# Narratica Audiobook App (Angular Frontend)

This README guides you step-by-step to set up a simple Angular frontend for an audiobook app. No special UI themes or external CSS frameworks—just Angular, standalone components, and SCSS.

---

## Table of Contents

1. Prerequisites  
2. Project Initialization  
3. Folder Structure  
4. Global Styles (SCSS)  
5. Creating Core Components  
6. Routing Setup  
7. Mock Data  
8. Audio Player Service & Component  
9. Running the App  
10. Next Steps  

---

## 1. Prerequisites

- **Node.js** (>=14.x) and **npm**  
- **Angular CLI** (>=17.x): `npm install -g @angular/cli`  
- Basic knowledge of TypeScript and Angular  

---

## 2. Project Initialization

1. Open a terminal and run:
   ```bash
   ng new narratica-app --routing=true --style=scss
   cd narratica-app
   ```
2. Choose **Standalone components** when prompted.

---

## 3. Folder Structure

Create minimal folders under `src/app`:

```
src/
└── app/
    ├── components/
    │   ├── navbar/
    │   └── player/
    ├── pages/
    │   ├── home/
    │   ├── login/
    │   ├── signup/
    │   ├── profile/
    │   └── book/
    └── services/
        └── audiobook.service.ts
```

Use:
```bash
mkdir -p src/app/components/navbar src/app/components/player          src/app/pages/{home,login,signup,profile,book}          src/app/services
```

---

## 4. Global Styles (SCSS)

1. Open `src/styles.scss` and replace with:

   ```scss
   /* Global CSS variables */
   :root {
     --primary-color: #F4B942;
     --background-light: #FFFFFF;
     --background-dark: #2D2D2D;
     --text-color: #2D2D2D;
   }

   body {
     margin: 0;
     font-family: 'Nunito', sans-serif;
     background: var(--background-light);
     color: var(--text-color);
   }

   .dark-mode {
     background: var(--background-dark);
     color: var(--background-light);
   }

   /* Utility classes */
   .container {
     max-width: 800px;
     margin: 0 auto;
     padding: 1rem;
   }
   ```

---

## 5. Creating Core Components

Use Angular CLI to generate standalone components:

```bash
ng generate component app/components/navbar --standalone
ng generate component app/components/player --standalone
ng generate component app/pages/home --standalone
ng generate component app/pages/login --standalone
ng generate component app/pages/signup --standalone
ng generate component app/pages/profile --standalone
ng generate component app/pages/book --standalone
```

- **NavbarComponent**: simple header with links.  
- **PlayerComponent**: fixed at bottom with mock controls.  

---

## 6. Routing Setup

1. In `src/app/app.routes.ts`, add:

   ```ts
   import { Routes } from '@angular/router';
   import { HomeComponent } from './pages/home/home.component';
   import { LoginComponent } from './pages/login/login.component';
   import { SignupComponent } from './pages/signup/signup.component';
   import { ProfileComponent } from './pages/profile/profile.component';
   import { BookComponent } from './pages/book/book.component';

   export const routes: Routes = [
     { path: '', component: HomeComponent },
     { path: 'login', component: LoginComponent },
     { path: 'signup', component: SignupComponent },
     { path: 'profile', component: ProfileComponent },
     { path: 'book/:id', component: BookComponent },
     { path: '**', redirectTo: '' }
   ];
   ```

2. In `main.ts`, bootstrap with router:

   ```ts
   import { bootstrapApplication } from '@angular/platform-browser';
   import { provideRouter } from '@angular/router';
   import { AppComponent } from './app/app.component';
   import { routes } from './app/app.routes';

   bootstrapApplication(AppComponent, {
     providers: [provideRouter(routes)]
   });
   ```

---

## 7. Mock Data

Place `audiobooks.json` in `src/assets/data/`:

```json
[
  { "id": 1, "title": "Sample Book", "author": "Author A" }
]
```

---

## 8. Audio Player Service & Component

1. **Service** `src/app/services/audiobook.service.ts`:
   ```ts
   import { Injectable } from '@angular/core';

   @Injectable({ providedIn: 'root' })
   export class AudiobookService {
     private audio = new Audio();

     play(url: string) { this.audio.src = url; this.audio.play(); }
     pause() { this.audio.pause(); }
   }
   ```

2. **PlayerComponent**: use buttons to call `play()`/`pause()` with a sample URL.

---

## 9. Running the App

```bash
ng serve
```

Open your browser at `http://localhost:4200`.

---

## 10. Next Steps

- Replace mock data with real API calls.  
- Add form validations for login/signup.  
- Implement dark mode toggle by adding/removing `.dark-mode` on `<body>`.  
- Refine player controls (seek bar, volume).

---

That's it! Even your grandma could follow these steps. Enjoy building!  
