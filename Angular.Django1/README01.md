# Narratica Audiobook App (Angular Frontend)

This README provides a step-by-step tutorial to set up the Angular frontend for the Narratica Audiobook App, including theming (light/dark mode), routing, mock data, and component structure. Anyone new to the project can follow these instructions to get a Proof of Concept (POC) up and running quickly.

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Project Initialization](#project-initialization)  
3. [Installing Dependencies](#installing-dependencies)  
4. [Project Structure](#project-structure)  
5. [Theming & Dark Mode](#theming--dark-mode)  
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
│   ├── data/audiobooks.json
│   └── covers/
└── styles/
    ├── _theme.scss
    └── styles.scss
```

---

## Theming & Dark Mode

1. **Define CSS variables** in `src/styles/_theme.scss`:
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
2. **Import theme** in `src/styles/styles.scss`:
   ```scss
   @import 'styles/theme';

   body {
     background-color: var(--color-background);
     color: var(--color-text);
     font-family: 'Nunito', sans-serif;
   }
   ```
3. **Include PrimeNG themes** in `angular.json`:
   ```json
   "styles": [
     "node_modules/primeng/resources/themes/saga-orange/theme.css",
     "node_modules/primeng/resources/themes/arya-orange/theme.css",
     "node_modules/primeng/resources/primeng.min.css",
     "node_modules/primeicons/primeicons.css",
     "src/styles/styles.scss"
   ]
   ```
4. **Create `ThemeService`** in `src/app/core/theme.service.ts` (see tutorial above).
5. **Build `ThemeToggleComponent`** in navbar, using a sun/moon icon button.

---

## Routing & Pages

Define routes in `src/app/app.routes.ts`:
```ts
import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', component: HomePage },
  { path: 'login', component: LoginPage },
  { path: 'signup', component: SignupPage },
  { path: 'profile', component: ProfilePage },
  { path: 'book/:id', component: BookPage },
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
