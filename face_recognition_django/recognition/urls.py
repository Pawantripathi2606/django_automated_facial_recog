from django.urls import path
from . import views

urlpatterns = [
    path('capture/<str:student_id>/', views.capture_photos, name='capture_photos'),
    path('save-photo/', views.save_photo, name='save_photo'),
    path('train/', views.train_model, name='train_model_page'),
    path('recognize/', views.recognize_face_view, name='recognize_face'),
    path('video-feed/', views.video_feed, name='video_feed'),
    path('recognition-events/', views.get_recognition_events, name='recognition_events'),
]

