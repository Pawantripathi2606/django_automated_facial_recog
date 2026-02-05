from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    """Form for creating and updating students"""
    
    class Meta:
        model = Student
        fields = [
            'student_id', 'name', 'department', 'course', 'year', 'semester',
            'division', 'roll_no', 'gender', 'dob', 'email', 'phone', 
            'address', 'teacher', 'photo_samples_taken'
        ]
        widgets = {
            'student_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student ID'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student Name'
            }),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'division': forms.Select(attrs={'class': 'form-select'}),
            'roll_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Roll Number'
            }),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 10-digit Phone Number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Enter Address'
            }),
            'teacher': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Teacher Name'
            }),
            'photo_samples_taken': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if phone and len(phone) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone
