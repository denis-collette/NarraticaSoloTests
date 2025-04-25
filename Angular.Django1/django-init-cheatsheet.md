# 🐍 Django Project Initialization Cheat Sheet

This guide walks you through the steps to initialize a Django project with best practices and beginner-friendly explanations.

---

## 🧰 Prerequisites

- Python 3.10+ installed
- `pip` (Python package manager)
- A virtual environment tool: `venv` (included with Python)
- Code editor (e.g., VS Code)
- Terminal or command prompt access

---

## 🚀 Project Setup

### 1. Create a Project Folder

```bash
mkdir my-django-project
cd my-django-project
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 3. Install Django

```bash
pip install django
```

> Optional but recommended: Create a `requirements.txt` file
```bash
pip freeze > requirements.txt
```

### 4. Start a New Django Project

```bash
django-admin startproject config .
```

> The `.` keeps the root clean by placing `manage.py` in the root folder.

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the Django welcome page.

---

## 🏗 Recommended File Structure

```
my-django-project/
│
├── config/           # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── app_name/         # Your main application (create it below)
├── manage.py         # Django CLI entry point
└── venv/             # Your virtual environment (don't touch)
```

### 6. Create a Django App

```bash
python manage.py startapp app_name
```

Then add your app to `INSTALLED_APPS` in `config/settings.py`.

### 7. Initial Database Migration

```bash
python manage.py migrate
```

---

## ⚙️ Common Setup Tips

- Create a `.gitignore` file and exclude `venv`, `__pycache__`, `.env`, etc.
- Use `.env` files to store secrets (with `python-decouple` or `django-environ`)
- Set up a superuser for admin access:

```bash
python manage.py createsuperuser
```

- Install useful packages (optional):
```bash
pip install djangorestframework
pip install python-decouple
```

---

## ✅ Next Steps

- Define your models in `models.py`
- Set up your routes in `urls.py`
- Create views and templates
- Explore Django Admin and Django REST Framework (for APIs)
