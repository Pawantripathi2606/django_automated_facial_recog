from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'department', 'course', 'semester', 'photo_samples_taken', 'created_at')
    list_filter = ('department', 'course', 'year', 'semester', 'division', 'gender', 'photo_samples_taken')
    search_fields = ('student_id', 'name', 'email', 'phone', 'roll_no')
    list_per_page = 25
    ordering = ('student_id',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Student Information', {
            'fields': ('student_id', 'name', 'gender', 'dob')
        }),
        ('Academic Details', {
            'fields': ('department', 'course', 'year', 'semester', 'division', 'roll_no', 'teacher')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address')
        }),
        ('Photo Sample', {
            'fields': ('photo_samples_taken',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
