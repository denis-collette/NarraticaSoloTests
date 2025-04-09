# Repository Structure and Cloning on Another Computer

## If your repository is structured like this:

```lua
Narratica/
├── App/
│   ├── Back(Django)/   <-- Django backend here
│   │   ├── manage.py
│   │   ├── requirements.txt
│   │   └── .gitignore
│   └── Front(React)/   <-- Next.js frontend here
│       ├── package.json
│       ├── package-lock.json
│       ├── .gitignore
│       └── ... (other frontend files)
└── .gitignore          <-- optional, for overall project if needed
```

## 1. On your current computer:

Commit all changes in both backend and frontend projects.

```bash
git add .
git commit -m "Checkpoint: ready to clone on new machine"
git push origin main
```

## 2. On your new computer:

### 1. Clone the repository:

```bash
git clone <repository_url>
cd Narratica
```

### 2. Backend setup:

- Navigate to the backend directory:

```bash
cd App/Back(Django)
```

- Set up a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

- Install Python dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

- Run database migrations and create a superuser (if using SQLite or another local DB):

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 3. Frontend setup:

- Navigate to the frontend directory:

```bash
cd ../Front(React)
```

- Install Node.js dependencies:

```bash
npm install
```

- Build or run the Next.js project:

```bash
npm run dev
```