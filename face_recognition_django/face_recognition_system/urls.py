from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def home(request):
    """Home page view"""
    from students.models import Student
    from attendance.models import Attendance
    from django.utils import timezone
    
    total_students = Student.objects.count()
    students_with_photos = Student.objects.filter(photo_samples_taken=True).count()
    today_attendance = Attendance.objects.filter(date=timezone.now().date()).count()
    recent_attendance = Attendance.objects.all()[:10]
    
    context = {
        'total_students': total_students,
        'students_with_photos': students_with_photos,
        'today_attendance': today_attendance,
        'recent_attendance': recent_attendance,
    }
    return render(request, 'home.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', include('students.urls')),
    path('recognition/', include('recognition.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
