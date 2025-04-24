# Narratica Audiobook App

Narratica is a full-stack audiobook streaming app built with **Angular** (frontend) and **Django** (backend). It aims to provide a smooth user experience for discovering, listening to, and managing audiobooks.

---

## 🛠️ Tech Stack

### Frontend
- **Angular 17+**
- **PrimeNG** UI library
- **SASS** for styling
- **Responsive / Mobile-First** design

### Backend
- **Django + Django REST Framework**
- PostgreSQL for database
- Hosted on Google Cloud or Render (WIP)

---

## 📁 Project Structure

```
Narratica-MountainProject/
├── App/
│   ├── Back/             # Django backend
│   └── Front/            # Angular frontend
│       ├── src/
│       └── angular.json  # Angular config
├── README.md
└── .gitignore
```

---

## 🎨 UI Theme

We are using the **Lara Light Indigo** theme from PrimeNG, which provides a clean and modern look that fits well with our audiobook platform's calm and engaging tone.

Theme file in use:
```scss
node_modules/primeng/resources/themes/lara-light-indigo/theme.css
```

---

## 🧑‍💻 Setup Instructions

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Run Angular frontend**:
   ```bash
   ng serve
   ```

3. **Run Django backend**:
   ```bash
   python manage.py runserver
   ```

---

## ✨ Features

- Listen to full audiobooks (if authorized) or short previews
- Public and private playlists
- Role-based access (Guest, User, Author, Admin)
- Upload and manage audio content (for Authors)
- Admin dashboard with full control
- Light/dark mode toggle (coming soon)

---

## 🎯 Goals

- **Educational**: Built as a learning project for junior devs.
- **Modular**: Easy to contribute to, scale, and maintain.
- **Accessible**: Usable on all screen sizes and devices.

---

## ✅ Contributors

- Denis Collette & BeCode Students – 2025  
- Stack: Angular | Django | PostgreSQL | PrimeNG

---

## 🧪 Notes

- This is a work-in-progress project.
- Social features (friends, sharing, etc.) are not yet implemented.

---