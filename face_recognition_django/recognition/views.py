from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from students.models import Student
from attendance.models import Attendance, TrainingModel
from .utils import FaceDetector, FaceRecognizer
import cv2
import os
import json
from datetime import datetime

def capture_photos(request, student_id):
    """View to capture photos for a student"""
    student = get_object_or_404(Student, student_id=student_id)
    context = {'student': student}
    return render(request, 'recognition/capture_photos.html', context)


@csrf_exempt
def save_photo(request):
    """API endpoint to save captured photo from browser"""
    if request.method == 'POST':
        try:
            import json
            import base64
            from PIL import Image
            from io import BytesIO
            import numpy as np
            
            data = json.loads(request.body)
            student_id = data.get('student_id')
            image_data = data.get('image')
            
            # Get student
            student = Student.objects.get(student_id=student_id)
            
            # Create training data directory
            training_dir = os.path.join(settings.MEDIA_ROOT, 'training_data')
            os.makedirs(training_dir, exist_ok=True)
            
            # Count existing photos for this student
            existing_photos = [f for f in os.listdir(training_dir) 
                              if f.startswith(f'user.{student.id}.')]
            photo_count = len(existing_photos)
            
            # Decode base64 image
            if ',' in image_data:
                image_data = image_data.split(',')[1]
            
            img_bytes = base64.b64decode(image_data)
            img = Image.open(BytesIO(img_bytes))
            
            # Convert to OpenCV format and detect face
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            detector = FaceDetector()
            faces = detector.detect_faces(img_cv)
            
            if len(faces) > 0:
                # Get first face
                x, y, w, h = faces[0]
                face_cropped = detector.crop_face(img_cv, (x, y, w, h))
                face_processed = cv2.resize(face_cropped, (450, 450))
                face_gray = cv2.cvtColor(face_processed, cv2.COLOR_BGR2GRAY)
                
                # Save image
                photo_count += 1
                filename = f'user.{student.id}.{photo_count}.jpg'
                filepath = os.path.join(training_dir, filename)
                cv2.imwrite(filepath, face_gray)
                
                # Auto-train if we have 100 photos (with atomic lock to prevent race condition)
                should_train = False
                if photo_count >= 100:
                    # Use atomic transaction with row-level lock to prevent duplicate training
                    from django.db import transaction
                    with transaction.atomic():
                        # Lock the student row to prevent concurrent updates
                        locked_student = Student.objects.select_for_update().get(id=student.id)
                        if not locked_student.photo_samples_taken:
                            locked_student.photo_samples_taken = True
                            locked_student.save()
                            should_train = True
                
                return JsonResponse({
                    'success': True, 
                    'count': photo_count,
                    'should_train': should_train,
                    'message': f'Photo {photo_count} saved successfully'
                })
            else:
                return JsonResponse({
                    'success': False, 
                    'error': 'No face detected in image'
                })
            
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Student not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})


@csrf_exempt
def train_model(request):
    """View to train the face recognition model"""
    if request.method == 'POST':
        try:
            recognizer = FaceRecognizer()
            training_data_path = os.path.join(settings.MEDIA_ROOT, 'training_data')
            
            success, num_images, num_students, accuracy = recognizer.train_model(training_data_path)
            
            if success:
                # Save training record with accuracy
                TrainingModel.objects.create(
                    model_file='models/classifier.xml',
                    num_students=num_students,
                    num_images=num_images,
                    accuracy=accuracy
                )
                
                # Check if this is an AJAX request
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': True,
                        'message': f'Model trained successfully! {num_images} images from {num_students} students.',
                        'num_images': num_images,
                        'num_students': num_students,
                        'accuracy': accuracy
                    })
                
                messages.success(request, f'Model trained successfully! {num_images} images from {num_students} students. Accuracy: {accuracy}%')
            else:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': 'No training data found'})
                messages.error(request, 'Training failed. No training data found.')
                
            if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
                return redirect('train_model_page')
                
        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': str(e)})
            messages.error(request, f'Error training model: {str(e)}')
            return redirect('train_model_page')
    
    # GET request - show training page
    training_models = TrainingModel.objects.all()[:10]
    total_students = Student.objects.filter(photo_samples_taken=True).count()
    
    context = {
        'training_models': training_models,
        'total_students': total_students
    }
    return render(request, 'recognition/train_model.html', context)


def recognize_face_view(request):
    """View for face recognition page"""
    return render(request, 'recognition/recognize.html')



# Global cache for recognition events (temporary storage for notifications)
# Format: {timestamp: {'student': student_obj, 'already_marked': bool, 'confidence': float}}
recognition_cache = []
recognition_cache_lock = __import__('threading').Lock()

def generate_frames():
    """Generator function to stream video frames"""
    from django.utils import timezone
    global recognition_cache
    
    detector = FaceDetector()
    recognizer = FaceRecognizer()
    recognizer.load_model()
    
    camera = cv2.VideoCapture(0)
    
    # Track recognized students in this session to avoid duplicate marks
    recognized_today = set()
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # Detect faces
        faces = detector.detect_faces(frame)
        
        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Recognize face
            face_roi = detector.crop_face(frame, (x, y, w, h))
            face_gray = detector.preprocess_face(face_roi)
            
            student_id, confidence = recognizer.recognize_face(face_gray)
            
            if confidence > 65:  # Confidence threshold
                try:
                    student = Student.objects.get(id=student_id)
                    
                    # Display student info
                    cv2.putText(frame, f"ID: {student.student_id}", (x, y-50), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(frame, f"Name: {student.name}", (x, y-30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(frame, f"Conf: {confidence:.1f}%", (x, y-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    
                    # Mark attendance (once per day per student)
                    if student.id not in recognized_today:
                        today = timezone.now().date()
                        attendance, created = Attendance.objects.get_or_create(
                            student=student,
                            date=today,
                            defaults={
                                'status': 'P',  # Present
                                'confidence': confidence
                            }
                        )
                        
                        if created:
                            recognized_today.add(student.id)
                            print(f"✓ Attendance marked for {student.name} ({student.student_id}) - Confidence: {confidence:.1f}%")
                            
                            # Add to recognition cache for notification
                            with recognition_cache_lock:
                                recognition_cache.append({
                                    'timestamp': timezone.now().isoformat(),
                                    'student_id': student.student_id,
                                    'student_name': student.name,
                                    'department': student.department,
                                    'already_marked': False,
                                    'confidence': round(confidence, 1)
                                })
                                # Keep only last 50 events
                                recognition_cache = recognition_cache[-50:]
                            
                            # Show "MARKED" text on video
                            cv2.putText(frame, "ATTENDANCE MARKED!", (x, y+h+30), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                        else:
                            # Already marked today - add to cache for duplicate notification
                            with recognition_cache_lock:
                                recognition_cache.append({
                                    'timestamp': timezone.now().isoformat(),
                                    'student_id': student.student_id,
                                    'student_name': student.name,
                                    'department': student.department,
                                    'already_marked': True,
                                    'confidence': round(confidence, 1),
                                    'marked_at': attendance.time.strftime('%I:%M %p')
                                })
                                recognition_cache = recognition_cache[-50:]
                            
                            # Show "Already Marked" text on video
                            cv2.putText(frame, "Already Marked Today", (x, y+h+30), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 165, 0), 2)
                    
                except Student.DoesNotExist:
                    cv2.putText(frame, "UNKNOWN", (x, y-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            else:
                cv2.putText(frame, "UNKNOWN", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    camera.release()


def video_feed(request):
    """Video streaming route"""
    return StreamingHttpResponse(generate_frames(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


@csrf_exempt
def get_recognition_events(request):
    """API endpoint to get recent recognition events for notifications"""
    global recognition_cache
    
    with recognition_cache_lock:
        events = list(recognition_cache)
        # Clear cache after reading
        recognition_cache = []
    
    return JsonResponse({'events': events})

