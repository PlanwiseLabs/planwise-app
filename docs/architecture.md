# Architecture

## Overview

Planwise follows a standard client-server architecture with a clear separation between the frontend, backend, and data layers.

```
┌──────────────────────────────────────────────────┐
│                    Browser                        │
│            Next.js 15 (TypeScript)               │
└───────────────────────┬──────────────────────────┘
                        │ HTTPS / REST
┌───────────────────────▼──────────────────────────┐
│                  FastAPI Backend                   │
│         Authentication · Tasks · Calendar         │
└──────────┬─────────────────────────┬─────────────┘
           │                         │
┌──────────▼──────────┐   ┌──────────▼──────────────┐
│     PostgreSQL       │   │   Google Calendar API    │
│  (primary database)  │   │   (OAuth 2.0 + REST)     │
└─────────────────────┘   └──────────────────────────┘
```

## Components

### Frontend (`/frontend`)

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Responsibilities**: Render UI, handle user input, communicate with the backend via REST.

### Backend (`/backend`)

- **Framework**: FastAPI
- **Language**: Python 3.12+
- **Responsibilities**: Expose REST API, apply priority logic, integrate with Google Calendar, manage authentication (JWT + Google OAuth 2.0).

### Database

- **Engine**: PostgreSQL 15
- **ORM**: SQLAlchemy 2 (async)
- **Migrations**: Alembic

### External Services

- **Google Calendar API** – read/write calendar events on behalf of the user.
- **Google OAuth 2.0** – user authentication.

## Data Flow

1. User logs in via Google OAuth 2.0 (frontend → backend → Google).
2. Backend issues a JWT and returns it to the frontend.
3. Frontend stores the JWT and sends it with every subsequent API request.
4. Backend validates the JWT, queries PostgreSQL, applies priority logic, and returns data.
5. For calendar operations, the backend calls the Google Calendar API with the user's stored OAuth token.
