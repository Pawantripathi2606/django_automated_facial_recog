# Face Recognition Attendance System - Django

A modern web-based face recognition attendance system built with Django, OpenCV, and Bootstrap 5.

## Features

✨ **Student Management**
- Add, edit, delete, and view student records
- Search functionality for quick lookups
- Comprehensive student profiles

🎥 **Face Recognition**
- Real-time face detection using webcam
- LBPH (Local Binary Patterns Histograms) algorithm
- Automatic attendance marking

📸 **Photo Capture**
- Capture multiple photo samples per student
- Training data collection interface
- Progress tracking

🧠 **Model Training**
- Train AI models with captured photos
- Training history tracking
- Model performance monitoring

📊 **Modern UI**
- Responsive Bootstrap 5 design
- Gradient color schemes
- Interactive dashboard
- Mobile-friendly interface

## Tech Stack

- **Backend**: Django 5.0.1
- **Database**: SQLite (default Django database)
- **Face Recognition**: OpenCV with opencv-contrib-python
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Icons**: Bootstrap Icons
- **Fonts**: Google Fonts (Inter)

## Installation

### Prerequisites

- Python 3.10 or higher
- Webcam (for photo capture and recognition)

### Setup Steps

1. **Navigate to project directory**
   ```bash
   cd face_recognition_django
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000`
   - Admin panel: `http://127.0.0.1:8000/admin`

## Usage Guide

### 🎯 Quick Start - Automated Workflow

**The entire system is now browser-based and fully automated!**

#### 1. Add Students (Web Interface)

1. Open your browser: `http://127.0.0.1:8000`
2. Navigate to **Students** → **Add New Student**
3. Fill in student details (ID, Name, Department, etc.)
4. Click **Create Student**

#### 2. Capture Photos (Automated - ~10 seconds)

1. Go to **Students** list
2. Click the 📷 camera icon for a student
3. Click **"Allow"** for webcam access
4. Click **"Start Capture"**

**What happens automatically:**
- ✅ Webcam opens in browser
- ✅ 100 photos captured in ~10 seconds
- ✅ Face detection ensures quality
- ✅ Progress bar shows real-time status
- ✅ **Model training starts automatically!**

#### 3. View Training Results

After photo capture completes:
- 🎓 Training happens automatically
- 📊 See statistics (images processed, students trained)
- ✅ Success message confirms completion

#### 4. Face Recognition (Live Video Feed)

1. Go to **Recognition** page
2. Click **"Start Recognition"**
3. Live video shows:
   - 🟢 Face detection rectangles
   - 👤 Student names and IDs
   - 📈 Confidence scores
   - ✅  Automatic attendance marking

---

### 📋 Manual Training (Optional)

If you want to retrain the model:

1. Go to **Train Model** page
2. Click **"Start Training"**
3. Wait for completion (~1-5 minutes)
4. View training statistics

---

### ⚙️ Admin Panel

Access advanced features at `http://127.0.0.1:8000/admin/`

- View detailed attendance records
- Manage students and training history
- Export data
- System configuration

---

## Key Features

✅ **Fully Automated** - No command-line interaction needed  
✅ **Browser-Based** - Works on any device with webcam  
✅ **Real-Time Feedback** - Progress bars and status updates  
✅ **Auto-Training** - Model trains automatically after photo capture  
✅ **Live Recognition** - Video stream with face detection  
✅ **Production-Ready** - Deploy to any web host

## Project Structure

```
face_recognition_django/
├── face_recognition_system/  # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── students/                 # Student management app
│   ├── models.py            # Student model
│   ├── views.py             # CRUD operations
│   ├── forms.py             # Student forms
│   └── admin.py             # Admin configuration
├── attendance/              # Attendance tracking
│   ├── models.py           # Attendance & Training models
│   └── admin.py
├── recognition/            # Face recognition
│   ├── utils.py           # OpenCV utilities
│   ├── views.py           # Recognition views
│   └── urls.py
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── students/
│   └── recognition/
├── static/               # CSS, JS, images
├── media/                # User uploads
│   ├── training_data/   # Captured photos
│   └── models/          # Trained models
├── db.sqlite3           # SQLite database
├── manage.py
└── requirements.txt
```

## Database Models

### Student
- student_id (unique)
- name, gender, dob
- department, course, year, semester, division
- email, phone, address
- teacher name
- photo_samples_taken (boolean)

### Attendance
- student (foreign key)
- date, time
- status (Present/Absent/Late)
- confidence (recognition accuracy)

### TrainingModel
- trained_at (timestamp)
- num_students, num_images
- model_file path

## Troubleshooting

### NumPy Compatibility Error

If you encounter a NumPy import error:
```bash
pip uninstall -y numpy
pip install numpy==1.24.3
```

### Webcam Not Detected

- Ensure webcam is properly connected
- Check browser permissions for webcam access
- Try a different browser (Chrome recommended)

### Model Not Training

- Verify photos are captured in `media/training_data/`
- Ensure at least 100 photos per student
- Check file naming format: `user.ID.number.jpg`

## Admin Panel

Access the admin panel at `/admin/` to:
- Manage students
- View attendance records
- Monitor training history
- Perform database operations

## Future Enhancements

- [ ] Export attendance to Excel/PDF
- [ ] Email notifications
- [ ] Multiple camera support
- [ ] Advanced analytics dashboard
- [ ] Mobile app integration
- [ ] Cloud deployment guides

## License

This project is created for educational purposes.

## Support

For issues or questions, please check the troubleshooting section above.
