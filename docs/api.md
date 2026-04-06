# API Reference

Base URL: `http://localhost:8000/api/v1`

Interactive documentation is available at `http://localhost:8000/api/docs` when the backend is running.

---

## Health

### `GET /health`

Returns the service health status.

**Response**
```json
{ "status": "ok" }
```

---

## Authentication

### `GET /auth/google`

Initiates the Google OAuth 2.0 login flow.

**Response**
```json
{ "url": "<google-oauth-authorization-url>" }
```

### `GET /auth/google/callback`

Handles the OAuth callback from Google and returns a JWT.

| Query Param | Type   | Description          |
|-------------|--------|----------------------|
| `code`      | string | Authorization code   |

**Response**
```json
{ "access_token": "<jwt>", "token_type": "bearer" }
```

---

## Tasks

### `GET /tasks`

Returns the list of tasks for the authenticated user.

**Response**
```json
[]
```

### `POST /tasks`

Creates a new task.

**Request Body**
```json
{
  "title": "string",
  "priority": "high | medium | low",
  "due_date": "2024-01-01T09:00:00Z"
}
```

**Response** – The created task object.
