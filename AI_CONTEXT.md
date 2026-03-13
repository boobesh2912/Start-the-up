# AI Context - Start The Up Builder Tracker

Start The Up Builder Tracker is a full-stack web app for a startup builder community. Cohort members log in, submit progress check-ins, track other builders, and view launched projects. The repo also includes public community pages (home, community, events, builders) and an admin dashboard for user/event management.

## Tech Stack

Frontend:
- Static HTML pages in `frontend/`
- TailwindCSS via CDN (`<script src="https://cdn.tailwindcss.com"></script>`)
- Vanilla JavaScript (`frontend/static/script.js` + inline page scripts)

Backend:
- FastAPI (`backend/app/main.py`)
- SQLAlchemy ORM and session management
- Pydantic schemas for request/response models

Database:
- PostgreSQL (Supabase connection string in `.env`)
- SQLAlchemy models mapped to tables: `users`, `checkins`, `events`

Authentication:
- JWT tokens (`python-jose`)
- Bearer token auth via `HTTPBearer`
- Password hashing with `passlib[bcrypt]`

Deployment notes in repo:
- README references frontend on Vercel and backend on Render/Railway
- `frontend/vercel.json` exists but is empty
- `backend/render.yaml` exists but is empty

## Repository Structure

```text
start the up/
  .env
  .gitignore
  README.md
  .venv/                         (local virtual env, ignored)
  backend/
    main.py
    requirements.txt
    render.yaml                  (empty)
    app/
      __init__.py
      main.py
      config.py
      database.py
      models/
        __init__.py
        user_model.py
        checkin_model.py
        event_model.py
        __pycache__/             (generated)
      schemas/
        __init__.py
        user_schema.py
        checkin_schema.py
        event_schema.py
        __pycache__/             (generated)
      routes/
        __init__.py
        auth_routes.py
        checkin_routes.py
        builder_routes.py
        launch_routes.py
        admin_routes.py
        events_routes.py
        __pycache__/             (generated)
      services/
        __init__.py
        auth_service.py
        checkin_service.py
        __pycache__/             (generated)
      __pycache__/               (generated)
  frontend/
    admin-dashboard.html
    builders.html
    checkin.html
    community.html
    dashboard.html
    events.html
    home.html
    launch-wall.html
    login.html
    vercel.json                  (empty)
    shared/
      navbar.html
      footer.html
    static/
      script.js
      styles.css
```

Major folder responsibilities:
- `backend/app/routes/`: FastAPI endpoint definitions.
- `backend/app/services/`: auth and check-in business logic.
- `backend/app/models/`: SQLAlchemy table models.
- `backend/app/schemas/`: Pydantic API contracts.
- `frontend/`: public pages, cohort pages, and admin page.
- `frontend/shared/`: reusable navbar/footer HTML loaded at runtime.
- `frontend/static/script.js`: API base config, auth helpers, shared fetch wrapper.

## Backend Architecture

Core backend files:
- `backend/app/main.py`: FastAPI app creation, CORS setup, router registration, `/health`, startup hooks.
- `backend/app/config.py`: loads root `.env` and exposes runtime settings.
- `backend/app/database.py`: SQLAlchemy engine/session/base and `get_db` dependency.
- `backend/app/models/*.py`: DB models (`User`, `Checkin`, `Event`).
- `backend/app/routes/*.py`: endpoint modules grouped by domain.
- `backend/app/services/auth_service.py`: password hashing, JWT creation/verification, auth dependencies.
- `backend/app/services/checkin_service.py`: create/read check-ins and compute builders/launch wall data.

Startup behavior (`backend/app/main.py`):
- Creates tables from SQLAlchemy metadata (`Base.metadata.create_all`).
- Runs `ensure_migrations()` to add `users.is_admin` if missing.
- Seeds an admin user using `ADMIN_EMAIL`/`ADMIN_PASSWORD` if not found.

Request lifecycle:
1. Client calls endpoint.
2. Route validates input via Pydantic schema.
3. Protected routes resolve user through `get_current_user` (Bearer JWT).
4. Route uses DB session dependency `get_db`.
5. Route/service queries or mutates SQLAlchemy models.
6. FastAPI serializes response using response models.

## Database Design

Database type in code: PostgreSQL via SQLAlchemy (not MongoDB).

### `users` table
Fields:
- `id` (PK, int)
- `name` (string, required)
- `email` (string, unique, indexed, required)
- `password_hash` (string, required)
- `project_name` (string, required)
- `cohort` (string, default `Cohort 1`)
- `is_admin` (boolean, default `False`)
- `created_at` (datetime)

### `checkins` table
Fields:
- `id` (PK, int)
- `user_id` (FK -> `users.id`, required)
- `update_text` (text, required)
- `demo_link` (string, nullable)
- `progress` (int, default `0`, clamped to `0..100` in service)
- `blocker` (text, nullable)
- `created_at` (datetime)

### `events` table
Fields:
- `id` (PK, int)
- `title` (string, required)
- `description` (text, required)
- `event_date` (datetime, required)
- `registration_link` (string, nullable)
- `status` (string, default `upcoming`)
- `created_at` (datetime)

Relationships:
- One `User` to many `Checkin` records (`Checkin.user` relationship + `User.checkins` backref).
- `Event` is standalone (no FK to users/checkins).

## API Endpoints

Auth legend:
- Public: no token
- User: requires valid Bearer token
- Admin: requires valid Bearer token for a user with `is_admin = true`

| Method | Path | Auth | Purpose | Request body | Response shape |
|---|---|---|---|---|---|
| GET | `/health` | Public | Health check | None | `{ "status": "ok" }` |
| POST | `/login` | Public | Authenticate and issue JWT | `{ email, password }` | `{ access_token, token_type }` |
| GET | `/me` | User | Current user profile | None | `UserResponse` |
| GET | `/users/me` | User | Alias of `/me` | None | `UserResponse` |
| POST | `/users` | Admin | Create user (compat/admin path) | `{ name, email, password, project_name, cohort, is_admin }` | `UserResponse` |
| POST | `/checkin` | User | Submit check-in | `{ update_text, demo_link?, progress, blocker? }` | `CheckinResponse` |
| POST | `/checkins/` | User | Alias of `/checkin` | `{ update_text, demo_link?, progress, blocker? }` | `CheckinResponse` |
| GET | `/checkins/me` | User | List current user check-ins (latest first) | None | `CheckinResponse[]` |
| GET | `/builders` | User | Builder progress board (latest check-in per user) | None | `BuilderStatus[]` |
| GET | `/checkins/builders` | User | Alias of `/builders` | None | `BuilderStatus[]` |
| GET | `/launch-wall` | User | Users whose latest check-in reached 100% | None | `LaunchEntry[]` |
| GET | `/checkins/launch-wall` | User | Alias of `/launch-wall` | None | `LaunchEntry[]` |
| GET | `/events` | Public | Upcoming events only (`status == "upcoming"`) | None | `EventResponse[]` |
| POST | `/admin/users` | Admin | Create user | `{ name, email, password, project_name, cohort, is_admin }` | `UserResponse` |
| GET | `/admin/users` | Admin | List all users | None | `UserResponse[]` |
| PUT | `/admin/users/{user_id}` | Admin | Update user | `{ name, email, password?, project_name, cohort, is_admin }` | `UserResponse` |
| DELETE | `/admin/users/{user_id}` | Admin | Delete user and their check-ins | None | `{ "status": "deleted" }` |
| POST | `/admin/events` | Admin | Create event | `{ title, description, event_date, registration_link?, status }` | `EventResponse` |
| GET | `/admin/events` | Admin | List all events | None | `EventResponse[]` |
| PUT | `/admin/events/{event_id}` | Admin | Update event (partial allowed) | Any subset of `{ title, description, event_date, registration_link, status }` | `EventResponse` |
| DELETE | `/admin/events/{event_id}` | Admin | Delete event | None | `{ "status": "deleted" }` |

## Frontend Architecture

Shared frontend runtime:
- `frontend/static/script.js` defines:
- `API_BASE = window.API_BASE || 'http://localhost:8000'`
- `apiFetch(path, options)` wrapper (adds `Authorization: Bearer <token>` when available)
- `requireAuth()`, `logout()`, `getToken()`
- `loadComponent(mountId, path)` for shared navbar/footer HTML

Page responsibilities:
- `frontend/home.html`: public landing page; loads shared navbar/footer; tries to show launch/event previews via `/launch-wall` and `/events`.
- `frontend/community.html`: public community/about page.
- `frontend/events.html`: public events page; fetches `/events` and renders dynamic event cards.
- `frontend/builders.html`: public builders page; if logged in, loads `/launch-wall` and `/builders`; otherwise shows placeholders and login prompt.
- `frontend/login.html`: login form; POSTs to `/login`; stores token in `localStorage` key `token`.
- `frontend/dashboard.html`: authenticated user dashboard; calls `/me`, `/checkins/me`, `/builders`.
- `frontend/checkin.html`: authenticated check-in form; POST `/checkin`; shows recent history via `/checkins/me`.
- `frontend/launch-wall.html`: authenticated launch wall page; loads `/launch-wall`.
- `frontend/admin-dashboard.html`: authenticated admin UI; validates admin via `/me`; manages users/events through `/admin/*` APIs.

How UI connects to backend:
- Most pages call `apiFetch(...)` from `frontend/static/script.js`.
- `login.html` uses direct `fetch` to `${API_BASE}/login`.
- On 401 from `apiFetch`, frontend clears token and redirects to `login.html`.

## Data Flow

Typical user flow:
1. User logs in on `frontend/login.html`.
2. Backend validates password hash and returns JWT from `POST /login`.
3. Frontend stores JWT in `localStorage` as `token`.
4. Protected pages call `requireAuth()` and then `apiFetch(...)`.
5. `apiFetch` sends `Authorization: Bearer <token>`.
6. Backend decodes JWT in `get_current_user`, fetches user from DB, and authorizes request.
7. Routes/services query PostgreSQL through SQLAlchemy and return JSON responses.
8. Frontend renders tables/cards/progress from returned data.

Admin flow:
1. `admin-dashboard.html` calls `/me` and checks `is_admin`.
2. Admin CRUD operations call `/admin/users*` and `/admin/events*`.
3. Backend enforces admin-only access with `get_admin_user`.

## Environment Variables

Defined in root `.env` and loaded by `backend/app/config.py`:
- `DATABASE_URL`: PostgreSQL connection string.
- `JWT_SECRET`: JWT signing secret.
- `JWT_ALGORITHM`: JWT algorithm (e.g., `HS256`).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: token expiry minutes.
- `ADMIN_EMAIL`: seeded admin email on startup.
- `ADMIN_PASSWORD`: seeded admin password on startup.

Notes:
- If `DATABASE_URL` starts with `postgres://`, code normalizes to `postgresql://`.
- Config includes safe defaults in `backend/app/config.py` if env vars are missing.

## Dependencies

From `backend/requirements.txt`:
- `fastapi`: API framework.
- `uvicorn`: ASGI server for running FastAPI.
- `sqlalchemy`: ORM and DB session layer.
- `psycopg2-binary`: PostgreSQL driver for SQLAlchemy.
- `python-dotenv`: loads `.env` values.
- `passlib[bcrypt]`: password hashing utilities.
- `bcrypt<4`: bcrypt version pin for compatibility.
- `email-validator`: validation for `EmailStr` in Pydantic schemas.
- `python-jose`: JWT encode/decode.
- `pydantic`: request/response data models and validation.

Frontend dependency model:
- No `package.json` in repo.
- Tailwind is loaded from CDN directly in HTML pages.

## Safe Modification Guidelines (IMPORTANT FOR AI)

- Keep existing route paths and compatibility aliases (`/checkins/*`, `/users/me`) unless explicitly asked to deprecate.
- Preserve auth enforcement on protected/admin endpoints.
- If schema fields change, update all three layers together: SQLAlchemy model, Pydantic schema, and affected frontend/API calls.
- Keep `apiFetch` token behavior (`Authorization` header + 401 logout redirect) intact.
- Do not remove startup admin seed/migration behavior without a replacement migration strategy.
- Maintain consistency between frontend fetch paths and backend route paths.
- Avoid hardcoding secrets in frontend or committing real credentials to docs/config.

## Feature Extension Guidelines

- Add new backend endpoints in `backend/app/routes/` and register the router in `backend/app/main.py` if new router module is created.
- Put reusable business logic in `backend/app/services/` instead of large route handlers.
- Add/extend DB models in `backend/app/models/` and corresponding API schemas in `backend/app/schemas/`.
- For new protected functionality, reuse `get_current_user` or `get_admin_user` dependencies.
- Add frontend page logic as small page-specific functions that call `apiFetch(...)`.
- Reuse shared UI fragments via `loadComponent` for navbar/footer where applicable.
- If adding new environment variables, document them in `README.md` and this file.
