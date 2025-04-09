# 🎧 Narratica – Audiobook Web App (Django + Next.js)

**Build a full-stack audiobook platform with Django (backend) and Next.js (frontend)**. This tutorial is designed for students finishing a 6-month course in web development.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [1. Project Setup](#1-project-setup)
- [2. Django Backend](#2-django-backend)
- [3. Next.js Frontend](#3-nextjs-frontend)
- [4. Private Library & Favorites](#4-private-library--favorites)
- [5. Media & Uploads (Bonus)](#5-media--uploads-bonus)
- [6. Extra Features](#6-extra-features)
- [7. Testing & Deployment](#7-testing--deployment)
- [8. HARD BONUS – Upload System for Users](#8-hard-bonus--upload-system-for-users)

---

## 🎯 Project Overview

**Narratica** is an audiobook streaming web app. It supports:

- Guest users (access to extracts only)
- Subscribed users (full access)
- Admin (full CRUD access)
- Audiobooks structured into chapters (each chapter is an audio file)
- Authors, Narrators, Publishers
- Favorites and personal library
- Optional upload system for users (bonus)

---

## 🧰 Tech Stack

### Backend
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT (auth)
- Pillow (image handling)
- django-storages (uploads, optional)

### Frontend
- Next.js
- Tailwind CSS
- Axios
- JWT for auth (manual)
- Optional: NextAuth

---

## 1. Project Setup

### 1.1 File Structure

```bash
Narratica/
├── backend/      # Django backend
├── frontend/     # Next.js frontend
└── README.md
```

### 1.2 Backend Setup

```bash
cd backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary pillow
django-admin startproject config .
python manage.py startapp core
```

### 1.3 Frontend Setup

```bash
cd ../
npx create-next-app@latest frontend
cd frontend
npm install axios
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Update tailwind.config.js and globals.css.

---

## 2. Django Backend

### 2.1 Configure Database (PostgreSQL)

In `backend/config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'narratica_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 2.2 Custom User Model
In `core/models.py`:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
```

In `settings.py`:

```python
AUTH_USER_MODEL = 'core.User'
```

### 2.3 Other Models

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Narrator(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    narrator = models.ForeignKey(Narrator, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Chapter(models.Model):
    audiobook = models.ForeignKey(Audiobook, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='chapters/')
    order = models.PositiveIntegerField()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audiobook = models.ForeignKey(Audiobook, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    narrator = models.ForeignKey(Narrator, null=True, blank=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.CASCADE)
```

### 2.4 API and Auth

```bash
pip install djangorestframework-simplejwt
```

In `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

Add endpoints for:

- `/auth/register/`, `/auth/login/`

- `/audiobooks/`, `/chapters/`

- `/favorites/`

Use serializers and viewsets (ModelViewSet or APIView).

---

## 3. Next.js Frontend

### 3.1 Tailwind Setup

In `globals.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 3.2 Authentication Pages

- `pages/login.tsx`

- `pages/register.tsx`

- Store JWT in `localStorage`

- Send token in `Authorization` header using Axios

### 3.3 Audiobook Pages

`pages/index.tsx`: Show featured books, latest extracts

`pages/audiobook/[id].tsx`: Detail page

`components/AudioPlayer.tsx`: Persistent audio player

### 3.4 Conditional Display

- Guests: extract only

- Subscribed: full access to chapters

- Show user’s library, favorites

---

## 4. Private Library & Favorites

### 4.1 Add/Remove API

- Endpoints: `/favorites/add/`, `/favorites/remove/`

- Retrieve user’s favorites in `/favorites/me/`

### 4.2 Frontend

- Heart icon to add/remove

- Separate page: `pages/library.tsx`

---

## 5. Media & Uploads (Bonus)

### 5.1 Setup for Uploads

- Use django-storages with:

    - Cloudinary

    - Google Cloud Storage

    - or local files (dev only)

### 5.2 Upload Page (Admin/Users)

- Admin or uploader page with a form:

    - Upload audiobook + thumbnail

    - Upload multiple chapters

--- 

## 6. Extra Features

### 🎨 Extract Background Color from Thumbnail

- Use Pillow in Django or JS lib (like `color-thief`) on frontend to extract dominant color from images

### 🎧 Always Visible Audio Player

- Add `AudioPlayer` to layout so it persists across pages

### 🌙 Dark Mode

- Use Tailwind’s `dark:` feature

Toggle with localStorage or context

---

## 7. Testing & Deployment

### 7.1 Testing

Use Postman to test endpoints

Create test users and try favorites/auth

### 7.2 Deployment Options

Component	Suggested Service
Backend	Render / Railway
Frontend	Vercel
DB	Supabase / GCP
Media	Cloudinary / GCP

---

## 8. HARD BONUS – Upload System for Users

1. Users can:

- Create new Audiobook

- Upload chapters

- Add author/narrator info

2. Requires:

- Upload form with progress bar

- Chapter ordering

- Validation rules

3. Use FormData in frontend + multipart/form-data in Django views

---

## 🙌 Credits

Made for students of a 6-month full-stack web dev program.
Feel free to fork, expand, and share your own versions of Narratica!