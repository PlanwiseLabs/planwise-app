# Planwise

> Automated routine organizer with priority-based scheduling and Google Calendar integration.

[![Backend](https://img.shields.io/badge/backend-FastAPI-009688?logo=fastapi)](./backend)
[![Frontend](https://img.shields.io/badge/frontend-Next.js-000000?logo=next.js)](./frontend)
[![Docs](https://img.shields.io/badge/docs-available-blue)](./docs)

---

## Overview

**Planwise** helps you take control of your day. It intelligently surfaces the most important tasks at the right time by combining a priority-based scheduling engine with seamless Google Calendar sync — so your routine adapts to you, not the other way around.

### Key Features

- 📋 **Priority-based task management** – create and rank tasks by urgency and importance
- 📅 **Google Calendar integration** – bi-directional sync so your schedule stays up to date
- 🔐 **Google OAuth 2.0** – sign in with your Google account
- ⚡ **Real-time API** – async FastAPI backend with interactive Swagger docs
- 🌐 **Modern web UI** – Next.js 15 with App Router and TypeScript

---

## Monorepo Structure

```
planwise-app/
├── backend/    # FastAPI (Python) – REST API, priority logic, Google Calendar integration
├── frontend/   # Next.js 15 (TypeScript) – web application
└── docs/       # Project documentation
```

| Directory | Technology | Purpose |
|-----------|-----------|---------|
| [`/backend`](./backend) | Python · FastAPI · PostgreSQL | REST API & business logic |
| [`/frontend`](./frontend) | TypeScript · Next.js 15 | Web interface |
| [`/docs`](./docs) | Markdown | Architecture, API reference, setup guide |

---

## Quick Start

### Prerequisites

| Tool | Version |
|------|---------|
| Python | ≥ 3.12 |
| Node.js | ≥ 20 |
| PostgreSQL | ≥ 15 |

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env   # then edit with your values
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

| Service | URL |
|---------|-----|
| Web app | http://localhost:3000 |
| REST API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/api/docs |

See the [Setup Guide](./docs/setup.md) for a full walkthrough including Google OAuth configuration.

---

## Documentation

- [Architecture](./docs/architecture.md)
- [API Reference](./docs/api.md)
- [Setup Guide](./docs/setup.md)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 15, React 19, TypeScript |
| Backend | FastAPI, Pydantic v2, SQLAlchemy 2 |
| Database | PostgreSQL 15 |
| Auth | Google OAuth 2.0, JWT |
| Calendar | Google Calendar API |

---

## License

[MIT](./LICENSE)
