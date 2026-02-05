from django.core.management.base import BaseCommand
from students.models import Student
import cv2
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Capture photo samples for a student using webcam'

    def add_arguments(self, parser):
        parser.add_argument('student_id', type=str, help='Student ID to capture photos for')

    def handle(self, *args, **options):
        student_id = options['student_id']
        
        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Student with ID {student_id} not found'))
            return

        self.stdout.write(self.style.SUCCESS(f'Starting photo capture for {student.name} ({student_id})'))
        
        # Create training data directory
        training_dir = os.path.join(settings.MEDIA_ROOT, 'training_data')
        os.makedirs(training_dir, exist_ok=True)
        
        # Initialize face detector
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Open webcam
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            self.stdout.write(self.style.ERROR('Could not open webcam'))
            return
        
        self.stdout.write(self.style.WARNING('Position your face in the camera...'))
        self.stdout.write(self.style.WARNING('Press ESC to stop early, or wait for 100 photos'))
        
        img_id = 0
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            
            for (x, y, w, h) in faces:
                # Draw rectangle on display frame
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Crop and save face
                face_cropped = frame[y:y+h, x:x+w]
                
                if face_cropped.size > 0:
                    img_id += 1
                    face_resized = cv2.resize(face_cropped, (450, 450))
                    face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                    
                    # Save with format: user.ID.number.jpg
                    file_name = f"user.{student.id}.{img_id}.jpg"
                    file_path = os.path.join(training_dir, file_name)
                    cv2.imwrite(file_path, face_gray)
                    
                    # Show progress on frame
                    cv2.putText(frame, f"Captured: {img_id}/100", (50, 50), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
                    if img_id % 10 == 0:
                        self.stdout.write(self.style.SUCCESS(f'Captured {img_id} photos...'))
            
            # Display frame
            cv2.imshow('Capturing Photos - Press ESC to stop', frame)
            
            # Break on ESC key or after 100 photos
            key = cv2.waitKey(1)
            if key == 27 or img_id >= 100:  # ESC key
                break
        
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        
        if img_id >= 100:
            # Update student record
            student.photo_samples_taken = True
            student.save()
            
            self.stdout.write(self.style.SUCCESS(
                f'Successfully captured {img_id} photos for {student.name}!'
            ))
            self.stdout.write(self.style.SUCCESS(
                f'Photos saved to: {training_dir}'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f'Only captured {img_id} photos (minimum 100 recommended)'
            ))
