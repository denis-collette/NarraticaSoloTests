# Narratica Audiobook App (Angular Frontend)

This README provides a step-by-step tutorial to set up the Angular frontend for the Narratica Audiobook App, including theming (light/dark mode), routing, mock data, and component structure. Anyone new to the project can follow these instructions to get a Proof of Concept (POC) up and running quickly.

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Project Initialization](#project-initialization)  
3. [Installing Dependencies](#installing-dependencies)  
4. [Project Structure](#project-structure)  
5. [Theming & Dark Mode](#theming--dark-mode)  
   - [5.1 Define Theme Variables](#define-theme-variables)  
   - [5.2 Create ThemeService](#create-themeservice)  
   - [5.3 Build ThemeToggleComponent](#build-themetogglecomponent)  
6. [Routing & Pages](#routing--pages)  
7. [Mock Data Setup](#mock-data-setup)  
8. [Core Components](#core-components)  
9. [Running the App](#running-the-app)  
10. [Next Steps](#next-steps)  

---

## Prerequisites

- Node.js (>= 14.x) and npm  
- Angular CLI (>= 15.x)  
- Basic familiarity with Angular and SCSS  

---

## Project Initialization

1. **Create the Angular app**  
   ```bash
   ng new narratica-audiobook-app --style=scss --routing=true
   cd narratica-audiobook-app
   ```
2. **Use standalone components**  
   Angular CLI will prompt; select standalone component support.

---

## Installing Dependencies

Install PrimeNG, icons, and PrimeFlex:
```bash
npm install primeng primeicons primeflex
```

---

## Project Structure

```
src/
├── app/
│   ├── core/
│   │   └── theme.service.ts
│   ├── components/
│   │   ├── navbar/
│   │   │   └── theme-toggle/
│   │   └── player/
│   ├── pages/
│   │   ├── home/
│   │   ├── login/
│   │   ├── signup/
│   │   ├── profile/
│   │   └── book/
│   ├── shared/
│   │   └── audiobook-card/
│   ├── app.component.ts
│   └── app.routes.ts
├── assets/
│   ├── data/
│   └── covers/
└── styles/
    ├── _theme.scss
    └── styles.scss
```

---

## Theming & Dark Mode

### 5.1 Define Theme Variables

1. **Create** `src/styles/_theme.scss`:
   ```scss
   :root {
     --color-primary: #F4B942;
     --color-secondary: #EF7C78;
     --color-tertiary: #70B9C1;
     --color-background: #FDF6E3;
     --color-text: #2D2D2D;
     --color-accent: #FF9244;
   }

   .dark-theme {
     --color-background: #2D2D2D;
     --color-text: #FDF6E3;
   }
   ```
2. **Import** in `src/styles/styles.scss`:
   ```scss
   @import 'styles/theme';

   body {
     background-color: var(--color-background);
     color: var(--color-text);
     font-family: 'Nunito', sans-serif;
   }
   ```

### 5.2 Create ThemeService

1. **Generate the service**:
   ```bash
   ng generate service app/core/theme --flat=false
   ```
2. **Implement** `src/app/core/theme.service.ts`:
   ```ts
   import { Injectable } from '@angular/core';

   @Injectable({
     providedIn: 'root'
   })
   export class ThemeService {
     private storageKey = 'theme';

     constructor() {
       const stored = localStorage.getItem(this.storageKey);
       if (stored === 'dark') {
         this.enableDark();
       }
     }

     toggle(): void {
       if (document.body.classList.contains('dark-theme')) {
         this.disableDark();
       } else {
         this.enableDark();
       }
     }

     enableDark(): void {
       document.body.classList.add('dark-theme');
       localStorage.setItem(this.storageKey, 'dark');
     }

     disableDark(): void {
       document.body.classList.remove('dark-theme');
       localStorage.setItem(this.storageKey, 'light');
     }
   }
   ```

### 5.3 Build ThemeToggleComponent

1. **Generate the component**:
   ```bash
   ng generate component app/components/navbar/theme-toggle --standalone --export
   ```
2. **Implement** `src/app/components/navbar/theme-toggle/theme-toggle.component.ts`:
   ```ts
   import { Component } from '@angular/core';
   import { ThemeService } from '../../../core/theme/theme.service';

   @Component({
     selector: 'app-theme-toggle',
     standalone: true,
     template: `
       <button pButton type="button"
               (click)="theme.toggle()"
               [icon]="icon"
               class="p-button-text"
               aria-label="Toggle Dark/Light Theme">
       </button>
     `
   })
   export class ThemeToggleComponent {
     constructor(public theme: ThemeService) {}

     get icon(): string {
       return document.body.classList.contains('dark-theme') ? 'pi pi-sun' : 'pi pi-moon';
     }
   }
   ```
3. **Include** in your `NavbarComponent` template:
   ```html
   <header>
     <!-- existing nav links and logo -->
     <app-theme-toggle></app-theme-toggle>
   </header>
   ```

---

## Routing & Pages

### 6.1 Updated `app.routes.ts`

```ts
import { Routes } from '@angular/router';

// Import standalone components
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

---

## Mock Data Setup

Place `audiobooks.json` under `src/assets/data/`:
```json
[
  {
    "id": 1,
    "title": "Book Title 1",
    "author": "Author Name",
    "duration": 3600,
    "coverUrl": "assets/covers/book1.jpg",
    "audioUrl": "assets/audio/book1.mp3"
  }
]
```
Use `HttpClient` in `AudiobookService` to fetch this file.

---

## Core Components

- **NavbarComponent**: includes logo, `SearchBarComponent`, `ThemeToggleComponent`, and auth links.
- **PlayerComponent**: docked at bottom; controls for play/pause, skip, volume, seek bar.
- **AudiobookCardComponent**: reusable card for displaying book previews.
- **ThemeToggleComponent**: icon button toggling dark/light mode.

---

## Running the App

1. **Serve**  
   ```bash
   ng serve
   ```
2. **Open** in browser: `http://localhost:4200`

---

## Next Steps

- Replace mock JSON with real API calls to your Django backend.  
- Implement actual authentication flows.  
- Add user favorites, suggestions based on listening history.  
- Enhance mobile responsiveness and accessibility.

---

Feel free to adapt as needed, and happy coding!
