# Planwise – Backend

FastAPI application powering the Planwise API.

## Stack

- **FastAPI** – async web framework
- **SQLAlchemy 2** – async ORM
- **PostgreSQL** – primary database (via `asyncpg`)
- **Alembic** – database migrations
- **Pydantic v2** – data validation & settings

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL 15+

### Setup

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Copy environment variables
cp .env.example .env
# Edit .env with your values

# Run the development server
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.
Interactive docs: `http://localhost:8000/api/docs`

## Project Structure

```
backend/
├── main.py               # Application entry point
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
└── app/
    ├── api/
    │   ├── router.py         # Main API router
    │   └── endpoints/        # Route handlers
    │       ├── auth.py
    │       ├── health.py
    │       └── tasks.py
    ├── core/
    │   └── config.py         # App settings (pydantic-settings)
    ├── models/               # SQLAlchemy ORM models
    └── schemas/              # Pydantic request/response schemas
```

## Running Tests

```bash
pytest
```

## Linting

```bash
ruff check .
mypy .
```
