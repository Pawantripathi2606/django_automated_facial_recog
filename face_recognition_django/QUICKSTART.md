# Quick Start Guide - Face Recognition System

## Complete Workflow

Follow these steps in order to set up and use the face recognition system.

---

## Step 1: Start Django Server

```bash
cd face_recognition_django
python manage.py runserver
```

Keep this terminal running. You'll need additional terminals for other commands.

---

## Step 2: Add Students (Web Browser)

1. Open browser: `http://127.0.0.1:8000`
2. Click **Students** → **Add New Student**
3. Fill in student details (ID, Name, Department, etc.)
4. Click **Create Student**

Repeat for all students you want to add.

---

## Step 3: Capture Photos (New Terminal)

Open a **NEW terminal** (keep server running in the first one):

```bash
cd face_recognition_django
python manage.py capture_photos <STUDENT_ID>
```

**Example:**
```bash
python manage.py capture_photos 12345
```

**What happens:**
- Webcam window opens
- System captures 100 photos automatically
- Green rectangles show face detection
- Counter shows progress
- Press ESC to stop early

Repeat this command for each student.

---

## Step 4: Train Model (Same Terminal)

After capturing photos for at least one student:

```bash
python manage.py train_model
```

**What happens:**
- Processes all captured training photos
- Creates recognition model
- Saves to `media/models/classifier.xml`
- Shows statistics (students, images processed)

You only need to run this once after capturing all photos. If you add more students later, run it again.

---

## Step 5: Face Recognition (Same Terminal)

```bash
python manage.py recognize_faces
```

**What happens:**
- Webcam window opens with live feed
- Faces are detected (green rectangles)
- Recognized students show:
  - Name
  - Student ID
  - Confidence percentage
- Attendance marked automatically (once per day)
- Press ESC to stop

---

## Step 6: View Results (Web Browser)

Go back to your browser at `http://127.0.0.1:8000`:

- **Dashboard**: See statistics and recent attendance
- **Students**: View all registered students
- **Admin Panel** (`/admin/`): View detailed attendance records

---

## Terminal Commands Summary

| Command | Purpose |
|---------|---------|
| `python manage.py runserver` | Start Django web server |
| `python manage.py capture_photos <ID>` | Capture 100 photos for a student |
| `python manage.py train_model` | Train recognition model with all photos |
| `python manage.py recognize_faces` | Start face recognition & attendance |

---

## Tips

**Photo Capture:**
- Ensure good lighting
- Look at camera from different angles
- Change facial expressions slightly
- Don't move too fast

**Recognition Accuracy:**
- 65%+ confidence = recognized
- Higher confidence = better match
- Retrain model if accuracy is low
- Capture more photos for better results

---

## Troubleshooting

**Webcam not opening:**
- Check webcam is connected
- Close other applications using webcam
- Try running as administrator

**Model not training:**
- Ensure photos were captured (`media/training_data/`)
- Check photos are named: `user.ID.number.jpg`
- Verify at least 1 student has photos

**Recognition not working:**  
- Make sure model is trained first
- Check model file exists: `media/models/classifier.xml`
- Ensure good lighting when recognizing

---

## Full Example Workflow

```bash
# Terminal 1 - Start server
cd face_recognition_django
python manage.py runserver

# Browser - Add student ID 12345 via web interface

# Terminal 2 - Capture photos for student
cd face_recognition_django
python manage.py capture_photos 12345
# (Webcam opens, captures 100 photos, press ESC when done)

# Train the model
python manage.py train_model
# (Waits 1-5 minutes, shows success message)

# Start recognition
python manage.py recognize_faces
# (Webcam opens, recognizes faces, press ESC to stop)

# Browser - View attendance at http://127.0.0.1:8000
```

---

That's it! Your face recognition attendance system is now fully operational.
