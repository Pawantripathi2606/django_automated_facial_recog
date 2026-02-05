from django.core.management.base import BaseCommand
from recognition.utils import FaceRecognizer
from attendance.models import TrainingModel
from students.models import Student
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Train the face recognition model with captured photos'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting model training...'))
        
        training_data_path = os.path.join(settings.MEDIA_ROOT, 'training_data')
        
        if not os.path.exists(training_data_path):
            self.stdout.write(self.style.ERROR(f'Training data directory not found: {training_data_path}'))
            return
        
        # Count images
        image_files = [f for f in os.listdir(training_data_path) if f.endswith('.jpg')]
        
        if len(image_files) == 0:
            self.stdout.write(self.style.ERROR('No training images found. Please capture photos first.'))
            return
        
        self.stdout.write(self.style.WARNING(f'Found {len(image_files)} training images'))
        
        # Train model
        recognizer = FaceRecognizer()
        success, num_images, num_students = recognizer.train_model(training_data_path)
        
        if success:
            # Count students with photos
            total_students = Student.objects.filter(photo_samples_taken=True).count()
            
            # Save training record
            TrainingModel.objects.create(
                model_file='models/classifier.xml',
                num_students=num_students,
                num_images=num_images
            )
            
            self.stdout.write(self.style.SUCCESS(
                f'✓ Model trained successfully!'
            ))
            self.stdout.write(self.style.SUCCESS(
                f'  - Images processed: {num_images}'
            ))
            self.stdout.write(self.style.SUCCESS(
                f'  - Students: {num_students}'
            ))
            self.stdout.write(self.style.SUCCESS(
                f'  - Model saved to: media/models/classifier.xml'
            ))
        else:
            self.stdout.write(self.style.ERROR('Training failed. Please check the training data.'))
