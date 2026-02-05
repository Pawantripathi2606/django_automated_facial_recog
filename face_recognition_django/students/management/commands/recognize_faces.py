from django.core.management.base import BaseCommand
from recognition.utils import FaceDetector, FaceRecognizer
from students.models import Student
from attendance.models import Attendance
from django.utils import timezone
import cv2

class Command(BaseCommand):
    help = 'Start face recognition using webcam'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting face recognition...'))
        self.stdout.write(self.style.WARNING('Press ESC to stop'))
        
        # Initialize
        detector = FaceDetector()
        recognizer = FaceRecognizer()
        
        # Load model
        if not recognizer.load_model():
            self.stdout.write(self.style.ERROR('Could not load trained model. Please train the model first.'))
            return
        
        self.stdout.write(self.style.SUCCESS('Model loaded successfully'))
        
        # Open webcam
        camera = cv2.VideoCapture(0)
        
        if not camera.isOpened():
            self.stdout.write(self.style.ERROR('Could not open webcam'))
            return
        
        recognized_today = set()  # Track who we've already marked present today
        
        while True:
            success, frame = camera.read()
            if not success:
                break
            
            # Detect faces
            faces = detector.detect_faces(frame)
            
            for (x, y, w, h) in faces:
                # Draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Recognize face
                face_roi = detector.crop_face(frame, (x, y, w, h))
                face_gray = detector.preprocess_face(face_roi)
                
                student_id, confidence = recognizer.recognize_face(face_gray)
                
                if confidence > 65:  # Confidence threshold
                    try:
                        student = Student.objects.get(id=student_id)
                        
                        # Display info
                        cv2.putText(frame, f"{student.name}", (x, y-50), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        cv2.putText(frame, f"ID: {student.student_id}", (x, y-30), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        cv2.putText(frame, f"Conf: {confidence:.1f}%", (x, y-10), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        
                        # Mark attendance (once per day)
                        if student.id not in recognized_today:
                            today = timezone.now().date()
                            attendance, created = Attendance.objects.get_or_create(
                                student=student,
                                date=today,
                                defaults={
                                    'status': 'P',
                                    'confidence': confidence
                                }
                            )
                            
                            if created:
                                recognized_today.add(student.id)
                                self.stdout.write(self.style.SUCCESS(
                                    f'✓ Attendance marked for {student.name} ({confidence:.1f}%)'
                                ))
                    
                    except Student.DoesNotExist:
                        cv2.putText(frame, "UNKNOWN", (x, y-10), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                else:
                    cv2.putText(frame, "UNKNOWN", (x, y-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            
            # Display frame
            cv2.imshow('Face Recognition - Press ESC to stop', frame)
            
            # Break on ESC
            if cv2.waitKey(1) == 27:
                break
        
        # Cleanup
        camera.release()
        cv2.destroyAllWindows()
        
        self.stdout.write(self.style.SUCCESS(
            f'Recognition stopped. Total attendance marked: {len(recognized_today)}'
        ))
