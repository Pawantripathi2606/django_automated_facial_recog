from django.contrib import admin
from .models import Attendance, TrainingModel

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'time', 'status', 'confidence')
    list_filter = ('status', 'date')
    search_fields = ('student__name', 'student__student_id')
    date_hierarchy = 'date'
    list_per_page = 50
    ordering = ('-date', '-time')
    readonly_fields = ('date', 'time', 'confidence')

@admin.register(TrainingModel)
class TrainingModelAdmin(admin.ModelAdmin):
    list_display = ('trained_at', 'num_students', 'num_images', 'accuracy')
    list_filter = ('trained_at',)
    date_hierarchy = 'trained_at'
    readonly_fields = ('trained_at', 'num_students', 'num_images')
    ordering = ('-trained_at',)
