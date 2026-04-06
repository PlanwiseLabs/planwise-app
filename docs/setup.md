# Setup Guide

## Prerequisites

| Tool | Minimum Version |
|------|----------------|
| Python | 3.12 |
| Node.js | 20 |
| PostgreSQL | 15 |
| npm | 10 |

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/PlanwiseLabs/planwise-app.git
cd planwise-app
```

### 2. Start the database

```bash
# Using Docker (recommended)
docker run -d \
  --name planwise-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=planwise \
  -p 5432:5432 \
  postgres:15
```

### 3. Set up the backend

```bash
cd backend

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements-dev.txt

cp .env.example .env
# Edit .env with your database URL, secret key, and Google OAuth credentials

uvicorn main:app --reload --port 8000
```

### 4. Set up the frontend

```bash
cd ../frontend

npm install

cp .env.example .env.local
# Edit .env.local if your backend runs on a different port

npm run dev
```

### 5. Open the app

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/api/docs |

---

## Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or select an existing one).
3. Enable the **Google Calendar API** and **Google+ API**.
4. Create OAuth 2.0 credentials (Web Application type).
5. Add `http://localhost:8000/api/v1/auth/google/callback` as an authorized redirect URI.
6. Copy the **Client ID** and **Client Secret** into `backend/.env`.

---

## Running Tests

```bash
# Backend
cd backend
pytest

# Frontend type check
cd frontend
npm run type-check
```
