from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class Student(models.Model):
    """Model for storing student information"""
    
    # Department choices
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('CE', 'Civil Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('EE', 'Electrical Engineering'),
    ]
    
    # Course choices
    COURSE_CHOICES = [
        ('CS_GENERAL', 'Computer Science'),
        ('CS_AI_ML', 'CSE - AI/ML'),
        ('CS_IOT', 'CSE - IOT'),
        ('CS_AIDS', 'CSE - AIDS'),
        ('CS_DS', 'CSE - DS'),
        ('CE_CONSTRUCTION', 'Construction Engineering'),
        ('CE_STRUCTURAL', 'Structural Engineering'),
        ('CE_GEOTECHNICAL', 'Geotechnical Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('EE', 'Electrical Engineering'),
    ]
    
    # Year choices
    YEAR_CHOICES = [
        ('2020-21', '2020-21'),
        ('2021-22', '2021-22'),
        ('2022-23', '2022-23'),
        ('2023-24', '2023-24'),
        ('2024-25', '2024-25'),
        ('2025-26', '2025-26'),
        ('2026-27', '2026-27'),
    ]
    
    # Semester choices
    SEMESTER_CHOICES = [
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    ]
    
    # Division choices
    DIVISION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]
    
    # Gender choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    
    # Student fields
    student_id = models.CharField(max_length=50, unique=True, verbose_name="Student ID")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES, verbose_name="Department")
    course = models.CharField(max_length=20, choices=COURSE_CHOICES, verbose_name="Course")
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, verbose_name="Year")
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES, verbose_name="Semester")
    division = models.CharField(max_length=1, choices=DIVISION_CHOICES, verbose_name="Division")
    roll_no = models.CharField(max_length=50, verbose_name="Roll Number", blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    dob = models.DateField(verbose_name="Date of Birth")
    
    # Contact information
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits.")
    email = models.EmailField(validators=[EmailValidator()], verbose_name="Email")
    phone = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Phone Number")
    address = models.TextField(verbose_name="Address")
    
    # Additional information
    teacher = models.CharField(max_length=100, verbose_name="Teacher Name")
    photo_samples_taken = models.BooleanField(default=False, verbose_name="Photo Sample Taken")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['student_id']
        
    def __str__(self):
        return f"{self.student_id} - {self.name}"
