from django.db import models
from students.models import Student

class Attendance(models.Model):
    """Model for storing attendance records"""
    
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now_add=True, verbose_name="Date")
    time = models.TimeField(auto_now_add=True, verbose_name="Time")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P', verbose_name="Status")
    confidence = models.FloatField(verbose_name="Recognition Confidence", help_text="Face recognition confidence percentage")
    
    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance Records"
        ordering = ['-date', '-time']
        unique_together = ['student', 'date']  # One attendance per student per day
        
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.get_status_display()}"


class TrainingModel(models.Model):
    """Model for storing training model history"""
    
    trained_at = models.DateTimeField(auto_now_add=True, verbose_name="Training Date")
    model_file = models.CharField(max_length=255, verbose_name="Model File Path")
    num_students = models.IntegerField(verbose_name="Number of Students")
    num_images = models.IntegerField(verbose_name="Number of Images")
    accuracy = models.FloatField(null=True, blank=True, verbose_name="Model Accuracy")
    notes = models.TextField(blank=True, verbose_name="Training Notes")
    
    class Meta:
        verbose_name = "Training Model"
        verbose_name_plural = "Training Models"
        ordering = ['-trained_at']
        
    def __str__(self):
        return f"Model trained on {self.trained_at.strftime('%Y-%m-%d %H:%M')}"
