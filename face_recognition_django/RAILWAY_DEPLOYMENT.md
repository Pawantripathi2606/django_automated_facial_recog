# Railway Deployment Guide

## Prerequisites

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **GitHub Account**: Your code must be in a GitHub repository
3. **Git Installed**: For pushing code to GitHub

## Step-by-Step Deployment

### 1. Prepare Your Code

Make sure all changes are committed and pushed to GitHub:

```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 2. Create Railway Project

1. Go to [railway.app](https://railway.app) and sign in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Authorize Railway to access your GitHub account
5. Select your `face_recognition_django` repository
6. Railway will automatically detect it's a Python project

### 3. Add MySQL Database

1. In your Railway project dashboard, click **"+ New"**
2. Select **"Database"** → **"Add MySQL"**
3. Railway will create a MySQL database and automatically set the `DATABASE_URL` environment variable

### 4. Configure Environment Variables

In your Railway project settings, go to the **"Variables"** tab and add:

| Variable | Value | Notes |
|----------|-------|-------|
| `SECRET_KEY` | Generate a new one | Use Django's `get_random_secret_key()` or [djecrety.ir](https://djecrety.ir) |
| `DEBUG` | `False` | Production setting |
| `ALLOWED_HOSTS` | `your-app-name.up.railway.app` | Replace with your actual Railway domain |
| `PYTHON_VERSION` | `3.11.0` | Python version |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app-name.up.railway.app` | Replace with your actual Railway domain |

**Note**: `DATABASE_URL` is automatically set by Railway when you add the MySQL database.

### 5. Deploy

1. Railway will automatically deploy when you push to GitHub
2. Wait for the build to complete (usually 3-5 minutes)
3. Once deployed, you'll see a URL like: `https://your-app.up.railway.app`

### 6. Create Superuser (Admin Account)

After deployment, you need to create an admin account:

1. In Railway dashboard, go to your web service
2. Click the **"Deployments"** tab
3. Find the latest deployment and click the **"3 dots"** menu
4. Select **"View Logs"**
5. Click **"Shell"** or **"Terminal"** to open a terminal
6. Run:
   ```bash
   python manage.py createsuperuser
   ```
7. Follow the prompts to create admin credentials

### 7. Access Your Application

- **Homepage**: `https://your-app.up.railway.app`
- **Admin Panel**: `https://your-app.up.railway.app/admin`

## Post-Deployment Checklist

- [ ] Application loads without errors
- [ ] Admin panel is accessible
- [ ] Can log in with superuser credentials
- [ ] Can create student records
- [ ] Can upload student photos
- [ ] Face recognition functionality works
- [ ] Attendance records are saved

## Important Notes

### Media Files (Student Photos)

> [!WARNING]
> Railway's filesystem is **ephemeral**, meaning uploaded files (student photos) may be lost on redeployment.

**For Production Use**: Consider using cloud storage like:
- **AWS S3** with `django-storages`
- **Cloudinary** with `django-cloudinary-storage`
- **Railway Volumes** (persistent storage)

### Database Backups

Railway provides automatic backups for MySQL databases. You can also manually backup:

1. Go to your MySQL service in Railway
2. Click **"Data"** tab
3. Use the export functionality or connect with a MySQL client

## Troubleshooting

### Build Fails

**Check the logs** in Railway dashboard:
- Look for missing dependencies
- Verify `requirements.txt` is correct
- Ensure `nixpacks.toml` is present for OpenCV dependencies

### Application Crashes

1. Check Railway logs for errors
2. Verify all environment variables are set correctly
3. Ensure `ALLOWED_HOSTS` includes your Railway domain
4. Check database connection is working

### Static Files Not Loading

1. Make sure `whitenoise` is in `requirements.txt`
2. Verify `STATIC_ROOT` is configured in `settings.py`
3. Railway runs `python manage.py collectstatic` during build

### Database Connection Errors

1. Verify MySQL database is added to your project
2. Check `DATABASE_URL` environment variable exists
3. Ensure `pymysql` and `dj-database-url` are in `requirements.txt`

## Updating Your Deployment

To deploy updates:

```bash
git add .
git commit -m "Your update message"
git push origin main
```

Railway will automatically detect the push and redeploy.

## Environment Variables Reference

Generate a strong SECRET_KEY using Python:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use online generator: [djecrety.ir](https://djecrety.ir)

## Support

- **Railway Documentation**: [docs.railway.app](https://docs.railway.app)
- **Django Deployment**: [docs.djangoproject.com/en/stable/howto/deployment/](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

## Quick Command Reference

```bash
# Local development
python manage.py runserver

# Check deployment readiness
python manage.py check --deploy

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```
