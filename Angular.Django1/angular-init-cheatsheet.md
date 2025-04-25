# 🚀 Angular Project Initialization Cheat Sheet

## ✅ 1. Install Angular CLI
```bash
npm install -g @angular/cli
```

## 🚀 2. Create a New Angular Project
```bash
ng new my-angular-app
```
Choose:
- Add routing: Yes/No
- Style format: SCSS (recommended)

## 🧼 3. Navigate into the Project
```bash
cd my-angular-app
```

## 🛠️ 4. Serve the Application
```bash
ng serve
```
Visit: `http://localhost:4200`

## 📦 5. Install Extra Libraries (Optional)
```bash
npm install primeng primeicons   # UI library
npm install @angular/forms       # For form handling
npm install axios                # HTTP client (optional)
```

## 📁 6. Generate Standalone Components (Angular 15+)
```bash
ng generate component my-component --standalone
```

## 🎨 7. Use SCSS Styling
Use component `.scss` files or `src/styles.scss` for global styles.

## 📂 8. Recommended Folder Structure
```
src/
├── app/
│   ├── components/      👈 Reusable UI components (e.g., buttons, cards)
│   ├── pages/           👈 Route-based views (e.g., homepage, login, dashboard)
│   ├── services/        👈 Reusable logic like API calls
│   ├── app.component.ts
│   ├── app.routes.ts
│   ├── app.config.ts
│   └── ...
├── assets/
├── environments/
├── index.html
├── styles.scss
└── main.ts
```

## 📄 9. Useful Angular CLI Commands
```bash
ng generate component my-comp
ng generate service my-service
ng build
ng test
ng lint
```

---
Happy coding with Angular! 🎉