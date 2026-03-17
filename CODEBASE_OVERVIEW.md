# CODEBASE OVERVIEW

## 1. PROJECT SUMMARY
- This repository implements Start The Up, a builder-community platform where cohort members authenticate, submit progress updates, view other builders, manage scheduled check-in forms, and showcase completed launches; it also contains public marketing/community pages.
- Tech stack at a glance: static HTML + inline CSS + TailwindCSS CDN + vanilla JavaScript on the frontend; FastAPI + SQLAlchemy + Pydantic + PostgreSQL (Supabase URL in `.env`) + JWT auth (`python-jose`) + Passlib/bcrypt on the backend; Vercel and Render deployment configs are checked in.
- The codebase contains both a legacy free-form check-in flow (`/checkin`) and a newer scheduled-form workflow (`/admin/forms`, `/forms/*`).
- Config files present: `.env`, `.gitignore`, `README.md`, `AI_CONTEXT.md`, `backend/requirements.txt`, `backend/render.yaml`, `frontend/vercel.json`, and `.venv/pyvenv.cfg`.
- Config files not present: `package.json`, `pyproject.toml`, `.env.example`, `vite.config.*`, `tailwind.config.*`, and `tsconfig.*`.

---

## 2. FRONTEND

### Files & Folders
- `frontend/` — Static frontend root containing all HTML pages, shared fragments, and small runtime assets.
- `frontend/admin-dashboard.html` — Admin console for authenticated admins to manage users, scheduled check-in forms, and responses.
- `frontend/builders.html` — Public builders showcase that swaps between placeholders and live logged-in data.
- `frontend/checkin.html` — Legacy authenticated free-form check-in page backed by `/checkin` and `/checkins/me`.
- `frontend/community.html` — Public community and mission page.
- `frontend/dashboard.html` — Authenticated multi-tab member dashboard built around the scheduled forms workflow.
- `frontend/events.html` — Public events page that fetches `/events` and also displays hard-coded past events.
- `frontend/home.html` — Public landing page with hero, recent launches preview, and upcoming events preview.
- `frontend/launch-wall.html` — Authenticated launch-wall page for projects that reached 100% progress.
- `frontend/login.html` — Cohort login page that posts credentials to `/login` and stores a JWT.
- `frontend/vercel.json` — Vercel route configuration that serves `home.html` at `/`.
- `frontend/shared/` — Reusable HTML fragments loaded into pages with `loadComponent()`.
- `frontend/shared/footer.html` — Public footer fragment with page links and community links.
- `frontend/shared/navbar.html` — Public navbar fragment with desktop and mobile navigation.
- `frontend/static/` — Shared runtime assets for static pages.
- `frontend/static/config.js` — Chooses the API base URL based on hostname.
- `frontend/static/script.js` — Provides shared auth helpers, component loading, and the `apiFetch()` wrapper.
- `frontend/static/styles.css` — Unused placeholder stylesheet for future global overrides.

### Framework & Language
- Framework used: plain static HTML pages with vanilla JavaScript; no React, Next.js, or client-side framework is present.
- Language: HTML, CSS, and JavaScript.
- Build tool: none; pages are served as static files, Tailwind is loaded at runtime from the CDN, and `frontend/vercel.json` only defines routing behavior.

### Styling & UI
- CSS framework or library: TailwindCSS via CDN, augmented with large page-local `<style>` blocks and an unused placeholder `frontend/static/styles.css` file.
- Colour codes used: `#065F46`, `#07070d`, `#0a0a0f`, `#0f0f17`, `#111`, `#111111`, `#111118`, `#15803D`, `#16161f`, `#18181f`, `#1A1A1A`, `#1e1e28`, `#1E40AF`, `#22c55e`, `#252530`, `#2563EB`, `#2a2a38`, `#2d2d2d`, `#333`, `#34d399`, `#374151`, `#6B21A8`, `#6b6b80`, `#6B7280`, `#6c63ff`, `#7C2D12`, `#8b5cf6`, `#92400E`, `#9CA3AF`, `#9D174D`, `#B45309`, `#BBF7D0`, `#d1d5db`, `#D1FAE5`, `#DBEAFE`, `#DCFCE7`, `#E5E3DC`, `#E5E7EB`, `#e8e5de`, `#e8e8f0`, `#F0EDE6`, `#F3E8FF`, `#F3F4F6`, `#F9FAFB`, `#FAF9F6`, `#FAFAFA`, `#fbbf24`, `#FCD34D`, `#FCE7F3`, `#FDE68A`, `#FEF3C7`, `#ff6584`, `#FFF7ED`, `rgba(0,0,0,0.07)`, `rgba(0,0,0,0.08)`, `rgba(0,0,0,0.2)`, `rgba(108,99,255,0.12)`, `rgba(108,99,255,0.15)`, `rgba(108,99,255,0.3)`, `rgba(251,191,36,0.12)`, `rgba(255,101,132,0.1)`, `rgba(255,101,132,0.12)`, `rgba(255,101,132,0.2)`, `rgba(255,101,132,0.3)`, `rgba(255,255,255,0.02)`, `rgba(255,255,255,0.05)`, `rgba(26,26,26,0.06)`, `rgba(37,99,235,0.08)`, `rgba(52,211,153,0.1)`, `rgba(52,211,153,0.12)`, `rgba(52,211,153,0.25)`, `rgba(52,211,153,0.3)`
- Fonts used: `DM Sans`, `Instrument Serif`, `Inter`, `Syne`, `sans-serif`, `serif`
- Any UI component libraries: not defined

### Pages & Components
- `frontend/home.html` — Landing page with a marketing hero, launch preview cards, and upcoming-events preview cards.
- `frontend/community.html` — Mission and values page with calls to join the WhatsApp community.
- `frontend/events.html` — Public event list page that renders backend events plus a static past-events section.
- `frontend/builders.html` — Public builder showcase that reveals real launch/build data only for authenticated users.
- `frontend/login.html` — Standalone login screen for cohort members.
- `frontend/dashboard.html` — Primary logged-in dashboard for the scheduled form workflow, builder board, launch wall, and response history.
- `frontend/checkin.html` — Legacy free-form check-in submission screen with a five-entry history preview.
- `frontend/launch-wall.html` — Dedicated logged-in launch-wall grid for shipped projects.
- `frontend/admin-dashboard.html` — Admin-only control panel for user management, form scheduling, and response review.
- `frontend/shared/navbar.html` — Reusable public navigation fragment.
- `frontend/shared/footer.html` — Reusable public footer fragment.
- `frontend/static/config.js` — Runtime API-base bootstrapper used before the shared script.
- `frontend/static/script.js` — Shared helper library for loading fragments and making authenticated API requests.
- `frontend/static/styles.css` — Unused placeholder stylesheet with a single comment.

### Key Frontend Dependencies
- No `package.json` is present in the repository, so there is no package-managed frontend dependency list.
- `TailwindCSS` — version not defined; loaded directly from `https://cdn.tailwindcss.com` and used via utility classes plus inline custom CSS.
- `Google Fonts` — version not defined; `Instrument Serif`, `Inter`, `DM Sans`, and `Syne` are loaded from `fonts.googleapis.com`.

---

## 3. BACKEND

### Files & Folders
- `backend/` — Backend root containing deployment configuration, dependency metadata, and the app package.
- `backend/render.yaml` — Render service definition for deploying the FastAPI backend.
- `backend/requirements.txt` — Direct Python dependencies for the backend.
- `backend/app/` — Main backend package.
- `backend/app/__init__.py` — Backend package marker.
- `backend/app/config.py` — Loads environment variables and exports runtime settings.
- `backend/app/database.py` — Creates the SQLAlchemy engine, sessionmaker, and `Base`.
- `backend/app/main.py` — Creates the FastAPI app, enables CORS, registers routers, creates tables, and seeds the admin user.
- `backend/app/models/` — SQLAlchemy models for persistent data.
- `backend/app/models/__init__.py` — Aggregates model imports.
- `backend/app/models/checkin_form_model.py` — Defines `CheckinForm` and `FormResponse` tables with JSON question/answer payloads.
- `backend/app/models/checkin_model.py` — Defines the legacy `checkins` table.
- `backend/app/models/event_model.py` — Defines the `events` table.
- `backend/app/models/user_model.py` — Defines the `users` table.
- `backend/app/models/__pycache__/` — Generated bytecode cache for model modules.
- `backend/app/routes/` — FastAPI route modules grouped by feature area.
- `backend/app/routes/__init__.py` — Exports router objects for app registration.
- `backend/app/routes/admin_routes.py` — Admin CRUD for users and events.
- `backend/app/routes/auth_routes.py` — Authentication and current-user endpoints.
- `backend/app/routes/builder_routes.py` — Builder board endpoints.
- `backend/app/routes/checkin_routes.py` — Legacy check-in submission/history endpoints.
- `backend/app/routes/events_routes.py` — Public upcoming-events route definition; currently not mounted by `app.main`.
- `backend/app/routes/form_routes.py` — Scheduled check-in form administration and response endpoints.
- `backend/app/routes/launch_routes.py` — Launch-wall endpoints.
- `backend/app/routes/__pycache__/` — Generated bytecode cache for route modules.
- `backend/app/schemas/` — Pydantic schemas used to validate and serialize API payloads.
- `backend/app/schemas/__init__.py` — Aggregates schema imports.
- `backend/app/schemas/checkin_form_schema.py` — Schemas for question definitions, forms, and form responses.
- `backend/app/schemas/checkin_schema.py` — Schemas for legacy check-ins, builders, and launch entries.
- `backend/app/schemas/event_schema.py` — Schemas for event create/update/read flows.
- `backend/app/schemas/user_schema.py` — Schemas for login, tokens, and user CRUD.
- `backend/app/schemas/__pycache__/` — Generated bytecode cache for schema modules.
- `backend/app/services/` — Reusable business and auth logic.
- `backend/app/services/__init__.py` — Aggregates service exports.
- `backend/app/services/auth_service.py` — JWT, password-hash, and auth-dependency helpers.
- `backend/app/services/checkin_service.py` — Legacy check-in creation and builder/launch aggregation logic.
- `backend/app/services/__pycache__/` — Generated bytecode cache for service modules.
- `backend/app/__pycache__/` — Generated bytecode cache for top-level backend modules.

### Framework & Language
- Language: Python 3.11 (the checked-in virtual environment reports Python 3.11.9 in `.venv/pyvenv.cfg`).
- Framework: FastAPI.
- Entry point file: `backend/app/main.py` (served as `app.main:app` in `backend/render.yaml`).

### API Routes
| Method | Path | Auth | Registration Status | What it does |
|---|---|---|---|---|
| GET | `/health` | Public | Active | Returns `{"status": "ok"}` for health checks. |
| POST | `/login` | Public | Active | Authenticates a user and returns a bearer token. |
| GET | `/me` | Bearer user | Active | Returns the authenticated user record. |
| GET | `/users/me` | Bearer user | Active | Compatibility alias for `/me`. |
| POST | `/users` | Bearer admin | Active | Creates a user through the compatibility/admin path. |
| POST | `/checkin` | Bearer user | Active | Creates a legacy free-form check-in. |
| POST | `/checkins/` | Bearer user | Active | Compatibility alias for `/checkin`. |
| GET | `/checkins/me` | Bearer user | Active | Returns the authenticated user's legacy check-ins in reverse chronological order. |
| GET | `/builders` | Bearer user | Active | Returns one latest-progress builder summary per non-admin user. |
| GET | `/checkins/builders` | Bearer user | Active | Compatibility alias for `/builders`. |
| GET | `/launch-wall` | Bearer user | Active | Returns non-admin users whose latest check-in reached 100% progress. |
| GET | `/checkins/launch-wall` | Bearer user | Active | Compatibility alias for `/launch-wall`. |
| POST | `/admin/users` | Bearer admin | Active | Creates a new user. |
| GET | `/admin/users` | Bearer admin | Active | Lists all users ordered by creation date. |
| PUT | `/admin/users/{user_id}` | Bearer admin | Active | Updates a user and optionally resets their password. |
| DELETE | `/admin/users/{user_id}` | Bearer admin | Active | Deletes a user and deletes their legacy check-ins first. |
| POST | `/admin/events` | Bearer admin | Active | Creates an event. |
| GET | `/admin/events` | Bearer admin | Active | Lists all events ordered by `event_date`. |
| PUT | `/admin/events/{event_id}` | Bearer admin | Active | Partially updates an event. |
| DELETE | `/admin/events/{event_id}` | Bearer admin | Active | Deletes an event. |
| POST | `/admin/forms` | Bearer admin | Active | Creates a scheduled check-in form and auto-sets `close_at` to 24 hours after `publish_at`. |
| GET | `/admin/forms` | Bearer admin | Active | Lists all forms ordered by publish time descending. |
| PUT | `/admin/forms/{form_id}` | Bearer admin | Active | Updates a form and recomputes `close_at` from `publish_at`. |
| DELETE | `/admin/forms/{form_id}` | Bearer admin | Active | Deletes a form and cascades its responses. |
| GET | `/admin/forms/{form_id}/responses` | Bearer admin | Active | Lists responses for one form together with user details. |
| DELETE | `/admin/responses/{response_id}` | Bearer admin | Active | Deletes a single form response. |
| GET | `/forms/active` | Bearer user | Active | Returns the currently active scheduled check-in form. |
| GET | `/forms/active/status` | Bearer user | Active | Returns whether a form is active and whether the current user already submitted it. |
| POST | `/forms/{form_id}/respond` | Bearer user | Active | Submits one response to an active form; duplicate submissions are blocked. |
| GET | `/forms/my-responses` | Bearer user | Active | Returns the authenticated user's form responses ordered newest first. |
| GET | `/events` | Public | Defined but not mounted | Returns upcoming events in `events_routes.py`, but `app.main` does not include `events_router`, so this path is not active in the current FastAPI app. |

### Database
- Database used: PostgreSQL; the committed `.env` file contains a Supabase pooled PostgreSQL `DATABASE_URL`.
- ORM or query method: SQLAlchemy ORM with `SessionLocal`, declarative models, and direct session queries in routes/services.
- Models defined: `User`, `Checkin`, `Event`, `CheckinForm`, and `FormResponse`.
- Schemas defined: `LoginRequest`, `TokenResponse`, `UserResponse`, `CreateUserRequest`, `UserUpdate`, `CheckinCreate`, `CheckinResponse`, `BuilderStatus`, `LaunchEntry`, `EventCreate`, `EventUpdate`, `EventResponse`, `QuestionSchema`, `CheckinFormCreate`, `CheckinFormUpdate`, `CheckinFormResponse`, `FormResponseCreate`, `FormResponseOut`, and `FormResponseWithUser`.
- Storage notes: `checkin_forms.questions` and `form_responses.answers` are stored as JSON columns; `checkins` remain a separate legacy table for the older free-form workflow.

### Modules & Libraries
- `fastapi` — version 0.135.1; ASGI web framework used to define the API.
- `uvicorn` — version 0.41.0; ASGI server used to run the FastAPI app.
- `sqlalchemy` — version 2.0.48; ORM and session layer for PostgreSQL access.
- `psycopg2-binary` — version 2.9.11; PostgreSQL driver used by SQLAlchemy.
- `python-dotenv` — version 1.2.2; Loads environment variables from the root `.env` file.
- `passlib[bcrypt]` — version passlib 1.7.4; Password hashing helpers used for stored user passwords.
- `bcrypt<4` — version 3.2.2 installed; requirements constrain it to <4; Pinned bcrypt backend used by passlib for hashing compatibility.
- `email-validator` — version 2.3.0; Validates `EmailStr` fields in Pydantic schemas.
- `python-jose` — version 3.5.0; Encodes and decodes JWT access tokens.
- `pydantic` — version 2.12.5; Request/response validation and schema serialization.

### Key Architecture
- The backend uses a hybrid route/service structure: authentication and legacy check-in aggregation logic live in `backend/app/services/`, while form management and most admin CRUD logic live directly in route handlers.
- `backend/app/main.py` enables permissive CORS (`allow_origins=["*"]`, all methods, all headers), creates tables on startup, applies a lightweight `users.is_admin` migration with raw SQL, and seeds an admin account from environment variables if one does not already exist.
- The frontend talks to the backend over REST using `fetch`, either through the shared `apiFetch()` helper in `frontend/static/script.js` or page-local wrappers in `dashboard.html` and `admin-dashboard.html`.
- Authentication is JWT-based: `POST /login` issues a bearer token, the frontend stores it in `localStorage` under `token`, and protected requests send `Authorization: Bearer <token>`.
- Authorization is enforced with `get_current_user()` and `get_admin_user()` in `backend/app/services/auth_service.py`.
- There are two parallel check-in UX flows: `frontend/checkin.html` uses the legacy `/checkin` endpoints, while `frontend/dashboard.html` and `frontend/admin-dashboard.html` operate on the scheduled form system under `/admin/forms` and `/forms/*`.
- The public events page expects `GET /events`, but the router that defines this endpoint (`backend/app/routes/events_routes.py`) is not included in `app.include_router(...)`, so the route is currently defined in code but inactive in the running FastAPI app.

---

## 4. FULL FOLDER & FILE STRUCTURE
project-root/ -> Repository root for Start The Up.
|-- .git/ -> Local Git metadata, refs, logs, hooks, and object storage.
|   |-- gk/
|   |   \-- config -> GitKraken metadata for the local repository.
|   |-- hooks/
|   |   |-- applypatch-msg.sample -> Sample Git hook script.
|   |   |-- commit-msg.sample -> Sample Git hook script.
|   |   |-- fsmonitor-watchman.sample -> Sample Git hook script.
|   |   |-- post-update.sample -> Sample Git hook script.
|   |   |-- pre-applypatch.sample -> Sample Git hook script.
|   |   |-- pre-commit.sample -> Sample Git hook script.
|   |   |-- pre-merge-commit.sample -> Sample Git hook script.
|   |   |-- pre-push.sample -> Sample Git hook script.
|   |   |-- pre-rebase.sample -> Sample Git hook script.
|   |   |-- pre-receive.sample -> Sample Git hook script.
|   |   |-- prepare-commit-msg.sample -> Sample Git hook script.
|   |   |-- push-to-checkout.sample -> Sample Git hook script.
|   |   |-- sendemail-validate.sample -> Sample Git hook script.
|   |   \-- update.sample -> Sample Git hook script.
|   |-- info/
|   |   \-- exclude -> Local Git ignore rules for this clone.
|   |-- logs/
|   |   |-- refs/
|   |   |   |-- heads/
|   |   |   |   \-- main -> Git reflog entry recording ref history.
|   |   |   \-- remotes/
|   |   |       \-- origin/
|   |   |           \-- main -> Git reflog entry recording ref history.
|   |   \-- HEAD -> Git reflog entry recording ref history.
|   |-- objects/
|   |   |-- 05/ -> Git object fan-out directory.
|   |   |   \-- 7e97c29e34aa70c3b4d667d42b8aa79b106399 -> Git object storage entry.
|   |   |-- 06/ -> Git object fan-out directory.
|   |   |   \-- 4eb9553976377f124a67688a836483dd794e5f -> Git object storage entry.
|   |   |-- 10/ -> Git object fan-out directory.
|   |   |   \-- 114f3c3eabb92169acb8b1e4f41e76f06eb133 -> Git object storage entry.
|   |   |-- 15/ -> Git object fan-out directory.
|   |   |   |-- 5c8d7009d4258448f46424058cfd351bbdeebf -> Git object storage entry.
|   |   |   \-- a75fa97d411e42ce9ffc2131f2764930a6c8ed -> Git object storage entry.
|   |   |-- 17/ -> Git object fan-out directory.
|   |   |   \-- 893848d7ac5802cba53d52354fa9ff2c5ae489 -> Git object storage entry.
|   |   |-- 18/ -> Git object fan-out directory.
|   |   |   \-- ba3177d606555cd8f018406564f21dc140667a -> Git object storage entry.
|   |   |-- 19/ -> Git object fan-out directory.
|   |   |   \-- e104349351502ca0edc1604377edb196da7a87 -> Git object storage entry.
|   |   |-- 1c/ -> Git object fan-out directory.
|   |   |   \-- 502172aa172a2a7a279eb0abeb2c71fc6026ac -> Git object storage entry.
|   |   |-- 1e/ -> Git object fan-out directory.
|   |   |   \-- 9a9bb18f66833a61089841f439eb5007b60730 -> Git object storage entry.
|   |   |-- 1f/ -> Git object fan-out directory.
|   |   |   \-- 1f5ae037366b68a6017eecc2be10ed66cb1a72 -> Git object storage entry.
|   |   |-- 25/ -> Git object fan-out directory.
|   |   |   \-- 33258b78dcdd11b7c478f60010dbe0bac188c6 -> Git object storage entry.
|   |   |-- 29/ -> Git object fan-out directory.
|   |   |   \-- 67f5850c2c7bf16ad1cd19d4e2fd4e9c190361 -> Git object storage entry.
|   |   |-- 30/ -> Git object fan-out directory.
|   |   |   \-- 0e0f07ba43a59fa1a64ee6e170aaa2b1005b0a -> Git object storage entry.
|   |   |-- 36/ -> Git object fan-out directory.
|   |   |   \-- 2a79679e4aa7da13783edaf8cef78cc50a6820 -> Git object storage entry.
|   |   |-- 38/ -> Git object fan-out directory.
|   |   |   \-- cbeea749b5289c90c375954bdee48eb443595e -> Git object storage entry.
|   |   |-- 40/ -> Git object fan-out directory.
|   |   |   \-- 19d90f741b3499c74cd7135030734902e7fc42 -> Git object storage entry.
|   |   |-- 43/ -> Git object fan-out directory.
|   |   |   \-- f30929e001b98e50ee448cd353b3e3aaf84ea5 -> Git object storage entry.
|   |   |-- 46/ -> Git object fan-out directory.
|   |   |   \-- 79a56a30bd162bdf0c7e337be7e5d802bb0a2d -> Git object storage entry.
|   |   |-- 47/ -> Git object fan-out directory.
|   |   |   \-- b36a5cd577714e260d6240160b14e13b0156df -> Git object storage entry.
|   |   |-- 4c/ -> Git object fan-out directory.
|   |   |   \-- 2b2cdaf3d19392b5206f351e116363425de17e -> Git object storage entry.
|   |   |-- 52/ -> Git object fan-out directory.
|   |   |   \-- 95569f6e485b33ffa7ed72a735f099e7932f21 -> Git object storage entry.
|   |   |-- 55/ -> Git object fan-out directory.
|   |   |   \-- b65683e861096a1de39417392cbeb4aecd5c13 -> Git object storage entry.
|   |   |-- 5b/ -> Git object fan-out directory.
|   |   |   \-- 3ccf9554f6ea352437035a9d1aac34d7befc19 -> Git object storage entry.
|   |   |-- 61/ -> Git object fan-out directory.
|   |   |   \-- 49f3b1672a94e7196adfc68c59e0c739c45700 -> Git object storage entry.
|   |   |-- 62/ -> Git object fan-out directory.
|   |   |   \-- 96e39186fd74ab9a0a0464ed45f7e69f356a6c -> Git object storage entry.
|   |   |-- 66/ -> Git object fan-out directory.
|   |   |   |-- 1168d1494a04a1e5db91d3ea8fa851643c43c4 -> Git object storage entry.
|   |   |   |-- 4568ee2e15da1f008e2dabfdf04ac465f81a0a -> Git object storage entry.
|   |   |   \-- c1978db4f5f3d584962dc80a24b1e35a1e55b9 -> Git object storage entry.
|   |   |-- 6b/ -> Git object fan-out directory.
|   |   |   |-- 2d18c4dac11d1a92884401fe264e7a0ba6bbc8 -> Git object storage entry.
|   |   |   \-- e3c7b7cdb610b51721d7997f5ab1abc1e9192e -> Git object storage entry.
|   |   |-- 72/ -> Git object fan-out directory.
|   |   |   \-- 371b3036ef57c71fd6516cfe4ec48a29a6c3e1 -> Git object storage entry.
|   |   |-- 77/ -> Git object fan-out directory.
|   |   |   \-- a29dbf10301f77f0acb5523a631c252201e439 -> Git object storage entry.
|   |   |-- 79/ -> Git object fan-out directory.
|   |   |   \-- 9923f76e1ce94b86e541f3e275a7f5366206d5 -> Git object storage entry.
|   |   |-- 7c/ -> Git object fan-out directory.
|   |   |   \-- b654337f4d7ce0d2b14a22780c947656b1981a -> Git object storage entry.
|   |   |-- 7d/ -> Git object fan-out directory.
|   |   |   \-- 212cedada0386bcdfeae537083cca571b6d086 -> Git object storage entry.
|   |   |-- 81/ -> Git object fan-out directory.
|   |   |   \-- 332a627f2118bd80fb98d7f06f4c5e621b5eb1 -> Git object storage entry.
|   |   |-- 83/ -> Git object fan-out directory.
|   |   |   \-- e39ef7003df7536f0289a6b1ac6ece17ad2469 -> Git object storage entry.
|   |   |-- 85/ -> Git object fan-out directory.
|   |   |   \-- 3ba00e282a5a76fc92fc94c0829dcc63e7ef5c -> Git object storage entry.
|   |   |-- 86/ -> Git object fan-out directory.
|   |   |   \-- ff4fe09bd2f139e8843d8100dc53dc13c7be71 -> Git object storage entry.
|   |   |-- 8a/ -> Git object fan-out directory.
|   |   |   \-- 9ce602d52604fe2cc48dd97c8e89a130b6dc5f -> Git object storage entry.
|   |   |-- 92/ -> Git object fan-out directory.
|   |   |   \-- 9d7f2bcc96b8da678f327bd8428f16f1f511c6 -> Git object storage entry.
|   |   |-- 93/ -> Git object fan-out directory.
|   |   |   \-- 72164182be8d95a86f1d30dcfd8f1ccd6e618a -> Git object storage entry.
|   |   |-- 94/ -> Git object fan-out directory.
|   |   |   \-- dec6358a0f17e599bb3dc6661da11337f16d3c -> Git object storage entry.
|   |   |-- 95/ -> Git object fan-out directory.
|   |   |   \-- 4a27212158c1c0b276b4519ef8144c12ef0503 -> Git object storage entry.
|   |   |-- 9a/ -> Git object fan-out directory.
|   |   |   \-- 9646ed8d696839ede81b33f6f08cfab1df46dd -> Git object storage entry.
|   |   |-- 9b/ -> Git object fan-out directory.
|   |   |   \-- 8196dd472e18bdae1764ccc6ce19563d93aedf -> Git object storage entry.
|   |   |-- 9c/ -> Git object fan-out directory.
|   |   |   |-- 10a68d453758e49162efa153aa6b1dff613c24 -> Git object storage entry.
|   |   |   \-- 6e93c1d60d1a78e0ea54263e9c1f8ba2f337e4 -> Git object storage entry.
|   |   |-- a1/ -> Git object fan-out directory.
|   |   |   \-- 63b6ea6bf504bd433328edb1229dcd1b159d23 -> Git object storage entry.
|   |   |-- a4/ -> Git object fan-out directory.
|   |   |   \-- 6e233090752ecb02f4b8efa7831e5708bf2bfe -> Git object storage entry.
|   |   |-- a8/ -> Git object fan-out directory.
|   |   |   \-- 12e32bf02b1cb353c58e6571e8a51f1da4f63b -> Git object storage entry.
|   |   |-- aa/ -> Git object fan-out directory.
|   |   |   \-- 6ba887c55688c1dad01e241b5d7e9d673c0449 -> Git object storage entry.
|   |   |-- ac/ -> Git object fan-out directory.
|   |   |   \-- 3a6db7c7ade2f394f6bf425c883c64cd3af0d2 -> Git object storage entry.
|   |   |-- b6/ -> Git object fan-out directory.
|   |   |   |-- 5b6354cd2558085d4d026eb7260e13862c96c7 -> Git object storage entry.
|   |   |   \-- 819c8fc681a5c248cb416c863458c5d88d6d2b -> Git object storage entry.
|   |   |-- b7/ -> Git object fan-out directory.
|   |   |   \-- e48e8107469b40bc4aa7d6791ae4953a9d3009 -> Git object storage entry.
|   |   |-- bd/ -> Git object fan-out directory.
|   |   |   \-- a9291b16a1f96d755cea5fe6a4e9ff55d9e83b -> Git object storage entry.
|   |   |-- be/ -> Git object fan-out directory.
|   |   |   \-- 703dbafe3cb779c66d107d60fb94102138f4bc -> Git object storage entry.
|   |   |-- bf/ -> Git object fan-out directory.
|   |   |   \-- 17f7621da53fa3f89766d96f7e2c30632d4ff4 -> Git object storage entry.
|   |   |-- c0/ -> Git object fan-out directory.
|   |   |   \-- 4ad03d76a9bec65fb85aed24dd86ca6082b19b -> Git object storage entry.
|   |   |-- c1/ -> Git object fan-out directory.
|   |   |   |-- 7464688c5acc3f77c8a4cd58137771be4d51d4 -> Git object storage entry.
|   |   |   \-- 8ee74d9bf9a23b5ad34c0a3be4a18a4f58310a -> Git object storage entry.
|   |   |-- c8/ -> Git object fan-out directory.
|   |   |   \-- 97addf10a216c755314f4c0b466a045c333591 -> Git object storage entry.
|   |   |-- d2/ -> Git object fan-out directory.
|   |   |   \-- 5f6bd2ab7455b0f8b23385ecfbc34bb6278d49 -> Git object storage entry.
|   |   |-- d9/ -> Git object fan-out directory.
|   |   |   \-- 50595a68a5f825e00562ff8ad9b33d800565ab -> Git object storage entry.
|   |   |-- df/ -> Git object fan-out directory.
|   |   |   \-- 0572708e56e648bb2017fd861cf15175a34913 -> Git object storage entry.
|   |   |-- e0/ -> Git object fan-out directory.
|   |   |   \-- 9c7cdf5698db67dcf16e946a78f2fced44964d -> Git object storage entry.
|   |   |-- e2/ -> Git object fan-out directory.
|   |   |   \-- 0dbb279d88469b06f7b55d0026a7f52d647181 -> Git object storage entry.
|   |   |-- e3/ -> Git object fan-out directory.
|   |   |   \-- ec25c3d8a8b92a2e9b53c81170d20fc1f84779 -> Git object storage entry.
|   |   |-- e6/ -> Git object fan-out directory.
|   |   |   \-- 9de29bb2d1d6434b8b29ae775ad8c2e48c5391 -> Git object storage entry.
|   |   |-- e7/ -> Git object fan-out directory.
|   |   |   \-- aec91b6c3a4d6a6e97f8dd7f9f1eeca763e280 -> Git object storage entry.
|   |   |-- e8/ -> Git object fan-out directory.
|   |   |   \-- d3a7a3975492e4a209c9279c713d76b5acb7f5 -> Git object storage entry.
|   |   |-- ec/ -> Git object fan-out directory.
|   |   |   \-- 3797482399528313f547d2d474cf1ab3d596bb -> Git object storage entry.
|   |   |-- ed/ -> Git object fan-out directory.
|   |   |   \-- 50481eadde318950d5627fa72181ad0b4e1e79 -> Git object storage entry.
|   |   |-- f0/ -> Git object fan-out directory.
|   |   |   \-- 7c67aa1e3073dc1b11c5625c29f1f67578996c -> Git object storage entry.
|   |   |-- f6/ -> Git object fan-out directory.
|   |   |   \-- 6e0ffe437e8b8201c622a92fa8faad9191fd96 -> Git object storage entry.
|   |   |-- fc/ -> Git object fan-out directory.
|   |   |   \-- 0e54ddcc497923ce76f47ddaf1d8d3c90c6bcf -> Git object storage entry.
|   |   |-- fe/ -> Git object fan-out directory.
|   |   |   |-- 8886adaf246f67670c67733bfde9b953fd5ce2 -> Git object storage entry.
|   |   |   \-- e634d95c851b087655b176b238552c41387d43 -> Git object storage entry.
|   |   |-- ff/ -> Git object fan-out directory.
|   |   |   \-- 52c287439597132f26b7e79cbf0acf50d346be -> Git object storage entry.
|   |   |-- info/ -> Git object fan-out directory.
|   |   \-- pack/ -> Git object fan-out directory.
|   |-- refs/
|   |   |-- heads/
|   |   |   \-- main -> Commit hash referenced by the local main branch.
|   |   |-- remotes/
|   |   |   \-- origin/
|   |   |       \-- main -> Commit hash referenced by the remote-tracking origin/main branch.
|   |   \-- tags/
|   |-- COMMIT_EDITMSG -> Last commit message recorded in local Git metadata.
|   |-- config -> Git repository configuration.
|   |-- description -> Default Git repository description placeholder.
|   |-- HEAD -> Symbolic ref that points Git to the currently checked-out branch.
|   \-- index -> Git staging index containing the current tracked-file state.
|-- .venv/ -> Checked-in local Python virtual environment.
|   |-- Include/
|   |   \-- site/
|   |       \-- python3.11/
|   |           \-- greenlet/
|   |               \-- greenlet.h -> Include file exposed by an installed package.
|   |-- Lib/
|   |   \-- site-packages/
|   |       |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |-- six.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   \-- typing_extensions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |-- _distutils_hack/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- override.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- override.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- annotated_doc/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- main.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- main.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |-- annotated_doc-0.0.4.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- annotated_types/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- test_cases.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   \-- test_cases.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- annotated_types-0.7.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- anyio/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- from_thread.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- functools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- lowlevel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- pytest_plugin.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- to_interpreter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- to_process.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- to_thread.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- _backends/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _asyncio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- _trio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _asyncio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- _trio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _core/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _asyncio_selector_thread.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _contextmanagers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _eventloop.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _fileio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _resources.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _signals.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _sockets.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _streams.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _subprocesses.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _synchronization.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _tasks.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _tempfile.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _testing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- _typedattr.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _asyncio_selector_thread.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _contextmanagers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _eventloop.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _fileio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _resources.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _signals.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _sockets.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _streams.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _subprocesses.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _synchronization.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _tasks.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _tempfile.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _testing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- _typedattr.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- abc/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _eventloop.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _resources.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _sockets.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _streams.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _subprocesses.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _tasks.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- _testing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _eventloop.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _resources.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _sockets.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _streams.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _subprocesses.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _tasks.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- _testing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- streams/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- buffered.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- file.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- memory.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- stapled.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- text.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- tls.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- buffered.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- file.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- memory.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- stapled.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- text.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- tls.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- from_thread.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- functools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- lowlevel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- pytest_plugin.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- to_interpreter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- to_process.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- to_thread.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- anyio-4.12.1.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- bcrypt/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __about__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __about__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _bcrypt.pyd -> Native binary for an installed package.
|   |       |   |-- _bcrypt.pyi -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |-- bcrypt-3.2.2.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- LICENSE -> License or author text for an installed package.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- cffi/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _imp_emulation.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _shimmed_dist_utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- api.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- backend_ctypes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- cffi_opcode.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- commontypes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- cparser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- error.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ffiplatform.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- lock.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- model.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- pkgconfig.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- recompiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- setuptools_ext.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- vengine_cpy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- vengine_gen.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- verifier.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _cffi_errors.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- _cffi_include.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- _embedding.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- _imp_emulation.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _shimmed_dist_utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- api.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- backend_ctypes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- cffi_opcode.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- commontypes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- cparser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- error.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ffiplatform.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- lock.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- model.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- parse_c_type.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- pkgconfig.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- recompiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- setuptools_ext.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- vengine_cpy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- vengine_gen.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- verifier.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- cffi-2.0.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- AUTHORS -> License or author text for an installed package.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- click/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _termui_impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _textwrap.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _winconsole.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- decorators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- formatting.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- globals.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- parser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- shell_completion.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- termui.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- testing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _termui_impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _textwrap.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _winconsole.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- decorators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- formatting.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- globals.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- parser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- shell_completion.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- termui.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- testing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- click-8.3.1.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE.txt -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- colorama/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ansi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ansitowin32.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- initialise.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- win32.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- winterm.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- tests/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ansi_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ansitowin32_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- initialise_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- isatty_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- winterm_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ansi_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ansitowin32_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- initialise_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- isatty_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- winterm_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ansi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ansitowin32.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- initialise.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- win32.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- winterm.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- colorama-0.4.6.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE.txt -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- dns/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _asyncbackend.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _asyncio_backend.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _ddr.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _features.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _immutable_ctx.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _no_ssl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _tls_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _trio_backend.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- asyncbackend.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- asyncquery.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- asyncresolver.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- btree.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- btreezone.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- dnssec.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- dnssectypes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- e164.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- edns.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- entropy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- enum.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exception.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- flags.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- grange.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- immutable.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- inet.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ipv4.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ipv6.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- message.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- name.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- namedict.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- nameserver.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- node.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- opcode.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- query.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rcode.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rdata.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rdataclass.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rdataset.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rdatatype.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- renderer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- resolver.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- reversename.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rrset.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- serial.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- set.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- tokenizer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- transaction.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- tsig.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- tsigkeyring.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ttl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- update.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- versioned.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- win32util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- wire.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- xfr.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- zone.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- zonefile.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- zonetypes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- dnssecalgs/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cryptography.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ecdsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- eddsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- rsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cryptography.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ecdsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- eddsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- rsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- quic/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _asyncio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _sync.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- _trio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _asyncio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _sync.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- _trio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rdtypes/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dnskeybase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dsbase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- euibase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mxbase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- nsbase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- svcbbase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- tlsabase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- txtbase.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ANY/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- AFSDB.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- AMTRELAY.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- AVC.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- CAA.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- CDNSKEY.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- CDS.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- CERT.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- CNAME.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- CSYNC.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- DLV.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- DNAME.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- DNSKEY.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- DS.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- DSYNC.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- EUI48.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- EUI64.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- GPOS.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- HINFO.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- HIP.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- ISDN.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- L32.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- L64.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- LOC.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- LP.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- MX.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NID.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NINFO.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NS.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NSEC.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NSEC3.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NSEC3PARAM.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- OPENPGPKEY.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- OPT.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- PTR.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- RESINFO.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- RP.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- RRSIG.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- RT.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- SMIMEA.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- SOA.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- SPF.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- SSHFP.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- TKEY.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- TLSA.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- TSIG.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- TXT.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- URI.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- WALLET.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- X25.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- ZONEMD.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- AFSDB.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- AMTRELAY.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- AVC.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- CAA.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- CDNSKEY.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- CDS.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- CERT.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- CNAME.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- CSYNC.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- DLV.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- DNAME.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- DNSKEY.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- DS.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- DSYNC.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- EUI48.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- EUI64.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- GPOS.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- HINFO.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- HIP.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- ISDN.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- L32.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- L64.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- LOC.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- LP.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- MX.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NID.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NINFO.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NS.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NSEC.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NSEC3.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NSEC3PARAM.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- OPENPGPKEY.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- OPT.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- PTR.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- RESINFO.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- RP.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- RRSIG.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- RT.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- SMIMEA.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- SOA.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- SPF.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- SSHFP.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- TKEY.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- TLSA.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- TSIG.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- TXT.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- URI.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- WALLET.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- X25.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- ZONEMD.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- CH/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- A.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- A.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- IN/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- A.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- AAAA.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- APL.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- DHCID.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- HTTPS.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- IPSECKEY.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- KX.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NAPTR.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NSAP.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- NSAP_PTR.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- PX.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- SRV.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- SVCB.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- WKS.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- A.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- AAAA.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- APL.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- DHCID.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- HTTPS.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- IPSECKEY.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- KX.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NAPTR.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NSAP.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- NSAP_PTR.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- PX.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- SRV.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- SVCB.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- WKS.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dnskeybase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dsbase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- euibase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mxbase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- nsbase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- svcbbase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tlsabase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- txtbase.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _asyncbackend.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _asyncio_backend.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _ddr.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _features.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _immutable_ctx.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _no_ssl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _tls_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _trio_backend.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- asyncbackend.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- asyncquery.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- asyncresolver.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- btree.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- btreezone.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- dnssec.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- dnssectypes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- e164.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- edns.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- entropy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- enum.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exception.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- flags.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- grange.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- immutable.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- inet.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ipv4.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ipv6.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- message.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- name.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- namedict.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- nameserver.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- node.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- opcode.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- query.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rcode.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rdata.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rdataclass.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rdataset.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rdatatype.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- renderer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- resolver.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- reversename.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rrset.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- serial.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- set.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- tokenizer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- transaction.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- tsig.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- tsigkeyring.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ttl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- update.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- versioned.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- win32util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- wire.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- xfr.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- zone.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- zonefile.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- zonetypes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- dnspython-2.8.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- dotenv/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- cli.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ipython.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- main.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- parser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- variables.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- cli.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ipython.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- main.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- parser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- variables.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- ecdsa/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _rwlock.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _sha3.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- curves.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- der.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ecdh.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ecdsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- eddsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ellipticcurve.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- keys.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- numbertheory.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rfc6979.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ssh.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_curves.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_der.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_ecdh.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_ecdsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_eddsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_ellipticcurve.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_jacobi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_keys.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_malformed_sigs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_numbertheory.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_pyecdsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_rw_lock.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- test_sha3.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _rwlock.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _sha3.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- curves.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- der.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ecdh.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ecdsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- eddsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ellipticcurve.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- keys.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- numbertheory.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- rfc6979.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ssh.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_curves.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_der.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_ecdh.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_ecdsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_eddsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_ellipticcurve.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_jacobi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_keys.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_malformed_sigs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_numbertheory.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_pyecdsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_rw_lock.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- test_sha3.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- ecdsa-0.19.1.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- LICENSE -> License or author text for an installed package.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- email_validator/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- deliverability.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- rfc_constants.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- syntax.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- validate_email.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- deliverability.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- rfc_constants.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- syntax.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- validate_email.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- email_validator-2.3.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- fastapi/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- .agents/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- skills/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |       \-- fastapi/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |           |-- references/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |           |   |-- dependencies.md -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |           |   |-- other-tools.md -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |           |   \-- streaming.md -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |           \-- SKILL.md -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- applications.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- background.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- cli.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- concurrency.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- datastructures.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- encoders.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exception_handlers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- logger.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- param_functions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- params.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- requests.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- responses.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- routing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- sse.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- staticfiles.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- templating.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- testclient.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- websockets.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- _compat/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- shared.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- v2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- shared.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- v2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- dependencies/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- models.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- models.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- middleware/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- asyncexitstack.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- gzip.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- httpsredirect.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- trustedhost.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- wsgi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- asyncexitstack.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- gzip.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- httpsredirect.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- trustedhost.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- wsgi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- openapi/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- constants.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- docs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- models.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- constants.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- docs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- models.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- security/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- api_key.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- http.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- oauth2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- open_id_connect_url.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- api_key.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- http.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- oauth2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- open_id_connect_url.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- applications.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- background.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- cli.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- concurrency.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- datastructures.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- encoders.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exception_handlers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- logger.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- param_functions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- params.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- requests.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- responses.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- routing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- sse.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- staticfiles.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- templating.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- testclient.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- websockets.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- fastapi-0.135.1.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- greenlet/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- platform/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- setup_switch_x64_masm.cmd -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_aarch64_gcc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_alpha_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_amd64_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_arm32_gcc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_arm32_ios.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_arm64_masm.asm -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_arm64_masm.obj -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_arm64_msvc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_csky_gcc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_loongarch64_linux.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_m68k_gcc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_mips_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_ppc64_aix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_ppc64_linux.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_ppc_aix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_ppc_linux.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_ppc_macosx.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_ppc_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_riscv_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_s390_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_sh_gcc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_sparc_sun_gcc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_x32_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_x64_masm.asm -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_x64_masm.obj -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_x64_msvc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- switch_x86_msvc.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   \-- switch_x86_unix.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- tests/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fail_clearing_run_switches.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fail_cpp_exception.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fail_initialstub_already_started.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fail_slp_switch.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fail_switch_three_greenlets.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fail_switch_three_greenlets2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fail_switch_two_greenlets.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- leakcheck.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_contextvars.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_cpp.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_extension_interface.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_gc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_generator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_generator_nested.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_greenlet.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_greenlet_trash.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_interpreter_shutdown.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_leaks.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_stack_saved.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_throw.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_tracing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- test_weakref.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _test_extension.c -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- _test_extension.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |   |-- _test_extension_cpp.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |   |-- _test_extension_cpp.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- fail_clearing_run_switches.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fail_cpp_exception.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fail_initialstub_already_started.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fail_slp_switch.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fail_switch_three_greenlets.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fail_switch_three_greenlets2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fail_switch_two_greenlets.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- leakcheck.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_contextvars.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_cpp.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_extension_interface.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_gc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_generator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_generator_nested.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_greenlet.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_greenlet_trash.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_interpreter_shutdown.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_leaks.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_stack_saved.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_throw.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_tracing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- test_weakref.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _greenlet.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |-- CObjects.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_allocator.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_compiler_compat.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_cpython_compat.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_exceptions.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_internal.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_msvc_compat.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_refs.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_slp_switch.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- greenlet_thread_support.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- PyGreenlet.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- PyGreenlet.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- PyGreenletUnswitchable.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- PyModule.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- slp_platformselect.h -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TBrokenGreenlet.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TExceptionState.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TGreenlet.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TGreenlet.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TGreenletGlobals.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TMainGreenlet.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TPythonState.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TStackState.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TThreadState.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TThreadStateCreator.hpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- TThreadStateDestroy.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   \-- TUserGreenlet.cpp -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |-- greenlet-3.3.2.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- LICENSE -> License or author text for an installed package.
|   |       |   |   \-- LICENSE.PSF -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- h11/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _abnf.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _connection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _events.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _headers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _readers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _receivebuffer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _state.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- _writers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _abnf.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _connection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _events.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _headers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _readers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _receivebuffer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _state.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _writers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |-- h11-0.16.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE.txt -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- idna/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- codec.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- idnadata.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- intranges.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- package_data.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- uts46data.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- codec.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- idnadata.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- intranges.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- package_data.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   \-- uts46data.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- idna-3.11.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE.md -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- jose/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- constants.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- jwe.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- jwk.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- jws.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- jwt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- backends/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _asn1.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cryptography_backend.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ecdsa_backend.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- native.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- rsa_backend.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _asn1.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cryptography_backend.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ecdsa_backend.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- native.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- rsa_backend.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- constants.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- jwe.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- jwk.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- jws.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- jwt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- passlib/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- apache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- apps.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- context.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- hash.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- hosts.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ifc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- pwd.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- registry.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- totp.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- win32.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- _data/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- wordsets/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |       |-- bip39.txt -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |       |-- eff_long.txt -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |       |-- eff_prefixed.txt -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |       \-- eff_short.txt -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- crypto/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _md4.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- des.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- digest.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _blowfish/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _gen_files.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- unrolled.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _gen_files.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- unrolled.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- scrypt/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _builtin.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _gen_files.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- _salsa.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _builtin.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _gen_files.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- _salsa.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _md4.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- des.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- digest.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ext/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- django/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- models.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- models.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- handlers/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- argon2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- bcrypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cisco.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- des_crypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- digests.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- django.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fshp.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ldap_digests.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- md5_crypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- misc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mssql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mysql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- oracle.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- pbkdf2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- phpass.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- postgres.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- roundup.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- scram.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- scrypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sha1_crypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sha2_crypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sun_md5_crypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- windows.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- argon2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- bcrypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cisco.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- des_crypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- digests.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- django.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fshp.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ldap_digests.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- md5_crypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- misc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mssql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mysql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- oracle.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pbkdf2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- phpass.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- postgres.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- roundup.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- scram.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- scrypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sha1_crypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sha2_crypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sun_md5_crypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- windows.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- tests/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _test_bad_register.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- backports.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_apache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_apps.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_context.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_context_deprecated.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_crypto_builtin_md4.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_crypto_des.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_crypto_digest.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_crypto_scrypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_ext_django.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_ext_django_source.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_handlers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_handlers_argon2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_handlers_bcrypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_handlers_cisco.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_handlers_django.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_handlers_pbkdf2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_handlers_scrypt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_hosts.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_pwd.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_registry.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_totp.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_utils_handlers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_utils_md4.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_utils_pbkdf2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test_win32.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- tox_support.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _test_bad_register.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- backports.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sample1.cfg -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- sample1b.cfg -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- sample1c.cfg -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- sample_config_1s.cfg -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- test_apache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_apps.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_context.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_context_deprecated.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_crypto_builtin_md4.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_crypto_des.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_crypto_digest.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_crypto_scrypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_ext_django.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_ext_django_source.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_handlers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_handlers_argon2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_handlers_bcrypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_handlers_cisco.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_handlers_django.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_handlers_pbkdf2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_handlers_scrypt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_hosts.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_pwd.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_registry.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_totp.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_utils_handlers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_utils_md4.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_utils_pbkdf2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test_win32.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tox_support.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- utils/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- binary.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- decor.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- des.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- handlers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- md4.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- pbkdf2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- compat/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- _ordered_dict.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- _ordered_dict.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- binary.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- decor.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- des.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- handlers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- md4.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- pbkdf2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- apache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- apps.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- context.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- hash.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- hosts.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ifc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- pwd.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- registry.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- totp.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- win32.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- passlib-1.7.4.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- LICENSE -> License or author text for an installed package.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   |-- WHEEL -> Installed-package metadata file.
|   |       |   \-- zip-safe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |-- pip/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- __pip-runner__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- _internal/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- build_env.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- configuration.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- main.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- pyproject.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- self_outdated_check.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- wheel_builder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- cli/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- autocompletion.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base_command.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cmdoptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- command_context.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- main.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- main_parser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- parser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- progress_bars.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- req_command.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- spinners.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- status_codes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- autocompletion.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base_command.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cmdoptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- command_context.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- main.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- main_parser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- parser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- progress_bars.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- req_command.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- spinners.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- status_codes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- commands/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- check.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- completion.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- configuration.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- debug.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- download.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- freeze.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- hash.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- help.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- index.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- inspect.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- install.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- list.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- search.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- show.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- uninstall.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- check.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- completion.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- configuration.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- debug.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- download.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- freeze.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- hash.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- help.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- index.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- inspect.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- list.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- search.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- show.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- uninstall.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- distributions/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- installed.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- sdist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- installed.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- sdist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- index/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- collector.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- package_finder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- sources.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- collector.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- package_finder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- sources.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- locations/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _distutils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _sysconfig.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _distutils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _sysconfig.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- metadata/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- pkg_resources.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- importlib/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- _dists.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- _envs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- _dists.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- _envs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- pkg_resources.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- models/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- candidate.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- direct_url.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- format_control.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- index.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- installation_report.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- link.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- scheme.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- search_scope.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- selection_prefs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- target_python.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- candidate.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- direct_url.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- format_control.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- index.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- installation_report.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- link.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- scheme.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- search_scope.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- selection_prefs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- target_python.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- network/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- auth.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- download.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- lazy_wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- session.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- xmlrpc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- auth.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- download.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- lazy_wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- session.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- xmlrpc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- operations/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- check.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- freeze.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- prepare.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- build/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- build_tracker.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- metadata.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- metadata_editable.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- metadata_legacy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- wheel_editable.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- wheel_legacy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- build_tracker.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- metadata.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- metadata_editable.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- metadata_legacy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- wheel_editable.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- wheel_legacy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- editable_legacy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- editable_legacy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- check.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- freeze.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- prepare.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- req/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- constructors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- req_file.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- req_install.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- req_set.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- req_uninstall.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- constructors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- req_file.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- req_install.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- req_set.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- req_uninstall.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- resolution/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- legacy/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- resolver.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- resolver.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- resolvelib/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- candidates.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- factory.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- found_candidates.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- provider.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- reporter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- requirements.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- resolver.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- candidates.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- factory.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- found_candidates.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- provider.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- reporter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- requirements.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- resolver.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- utils/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _jaraco_text.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _log.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- appdirs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- compatibility_tags.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- datetime.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- deprecation.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- direct_url_helpers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- egg_link.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- encoding.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- entrypoints.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- filesystem.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- filetypes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- glibc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- hashes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- logging.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- misc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- models.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- packaging.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- setuptools_build.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- subprocess.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- temp_dir.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- unpacking.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- urls.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- virtualenv.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _jaraco_text.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _log.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- appdirs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- compatibility_tags.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- datetime.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- deprecation.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- direct_url_helpers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- egg_link.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- encoding.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- entrypoints.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- filesystem.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- filetypes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- glibc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- hashes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- logging.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- misc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- models.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- packaging.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- setuptools_build.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- subprocess.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- temp_dir.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- unpacking.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- urls.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- virtualenv.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- vcs/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- bazaar.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- git.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mercurial.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- subversion.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- versioncontrol.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- bazaar.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- git.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mercurial.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- subversion.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- versioncontrol.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- build_env.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- configuration.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- main.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pyproject.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- self_outdated_check.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- wheel_builder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _vendor/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- six.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- typing_extensions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- cachecontrol/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _cmd.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- adapter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- controller.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- filewrapper.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- heuristics.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- serialize.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wrapper.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- caches/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- file_cache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- redis_cache.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- file_cache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- redis_cache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _cmd.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- adapter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cache.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- controller.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- filewrapper.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- heuristics.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- serialize.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- wrapper.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- certifi/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cacert.pem -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |-- chardet/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- big5freq.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- big5prober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- chardistribution.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- charsetgroupprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- charsetprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- codingstatemachine.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- codingstatemachinedict.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cp949prober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- enums.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- escprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- escsm.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- eucjpprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- euckrfreq.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- euckrprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- euctwfreq.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- euctwprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- gb2312freq.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- gb2312prober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- hebrewprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- jisfreq.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- johabfreq.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- johabprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- jpcntx.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- langbulgarianmodel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- langgreekmodel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- langhebrewmodel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- langhungarianmodel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- langrussianmodel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- langthaimodel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- langturkishmodel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- latin1prober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- macromanprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mbcharsetprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mbcsgroupprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mbcssm.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- resultdict.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- sbcharsetprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- sbcsgroupprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- sjisprober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- universaldetector.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- utf1632prober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- utf8prober.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cli/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- chardetect.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- chardetect.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- metadata/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- languages.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- languages.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- big5freq.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- big5prober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- chardistribution.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- charsetgroupprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- charsetprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- codingstatemachine.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- codingstatemachinedict.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cp949prober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- enums.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- escprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- escsm.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- eucjpprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- euckrfreq.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- euckrprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- euctwfreq.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- euctwprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- gb2312freq.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- gb2312prober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- hebrewprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- jisfreq.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- johabfreq.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- johabprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- jpcntx.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- langbulgarianmodel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- langgreekmodel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- langhebrewmodel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- langhungarianmodel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- langrussianmodel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- langthaimodel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- langturkishmodel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- latin1prober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- macromanprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mbcharsetprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mbcsgroupprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mbcssm.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- resultdict.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- sbcharsetprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- sbcsgroupprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- sjisprober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- universaldetector.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- utf1632prober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- utf8prober.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- colorama/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- ansi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- ansitowin32.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- initialise.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- win32.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- winterm.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- tests/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- ansi_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- ansitowin32_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- initialise_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- isatty_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- winterm_test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- ansi_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- ansitowin32_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- initialise_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- isatty_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- winterm_test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- ansi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- ansitowin32.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- initialise.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- win32.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- winterm.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- distlib/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- database.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- index.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- locators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- manifest.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- markers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- metadata.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- resources.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- scripts.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- database.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- index.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- locators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- manifest.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- markers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- metadata.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- resources.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- scripts.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- t32.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |   |-- t64-arm.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |   |-- t64.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |   |-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- w32.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |   |-- w64-arm.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |   |-- w64.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |   \-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- distro/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- distro.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- distro.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |-- idna/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- codec.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- idnadata.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- intranges.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- package_data.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- uts46data.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- codec.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- idnadata.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- intranges.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- package_data.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   \-- uts46data.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- msgpack/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- ext.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- fallback.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- ext.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- fallback.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- packaging/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __about__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _manylinux.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _musllinux.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _structures.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- markers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- requirements.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- specifiers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- tags.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __about__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _manylinux.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _musllinux.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _structures.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- markers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- requirements.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- specifiers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- tags.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pkg_resources/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- platformdirs/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- android.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- api.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- macos.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- unix.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- windows.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- android.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- api.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- macos.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- unix.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- windows.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pygments/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cmdline.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- console.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- filter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- formatter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- lexer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- modeline.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- plugin.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- regexopt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- scanner.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- sphinxext.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- style.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- token.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- unistring.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- filters/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- formatters/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- _mapping.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- bbcode.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- groff.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- html.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- img.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- irc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- latex.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- other.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- pangomarkup.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- rtf.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- svg.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- terminal.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- terminal256.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- _mapping.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- bbcode.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- groff.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- html.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- img.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- irc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- latex.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- other.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- pangomarkup.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- rtf.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- svg.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- terminal.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- terminal256.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- lexers/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- _mapping.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- python.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- _mapping.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- python.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- styles/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cmdline.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- console.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- filter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- formatter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- lexer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- modeline.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- plugin.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- regexopt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- scanner.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- sphinxext.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- style.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- token.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- unistring.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pyparsing/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- actions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- helpers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- results.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- testing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- unicode.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- diagram/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- actions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- helpers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- results.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- testing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- unicode.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pyproject_hooks/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- _impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _in_process/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- _in_process.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- _in_process.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- _impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- requests/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __version__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _internal_utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- adapters.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- api.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- auth.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- certs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cookies.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- help.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- hooks.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- models.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- packages.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- sessions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- status_codes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- structures.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __version__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _internal_utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- adapters.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- api.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- auth.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- certs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cookies.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- help.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- hooks.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- models.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- packages.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- sessions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- status_codes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- structures.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- resolvelib/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- providers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- reporters.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- resolvers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- structs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- compat/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- collections_abc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- collections_abc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- providers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- reporters.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- resolvers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- structs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- rich/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _cell_widths.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _emoji_codes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _emoji_replace.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _export_format.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _extension.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _fileno.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _inspect.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _log_render.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _loop.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _null_file.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _palettes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _pick.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _ratio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _spinners.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _stack.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _timer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _win32_console.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _windows.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _windows_renderer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _wrap.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- abc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- align.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- ansi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- bar.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- box.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cells.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- color.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- color_triplet.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- columns.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- console.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- constrain.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- containers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- control.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- default_styles.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- diagnose.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- emoji.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- file_proxy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- filesize.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- highlighter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- jupyter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- layout.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- live.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- live_render.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- logging.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- markup.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- measure.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- padding.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pager.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- palette.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- panel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pretty.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- progress.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- progress_bar.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- prompt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- protocol.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- region.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- repr.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- rule.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- scope.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- screen.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- segment.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- spinner.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- status.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- style.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- styled.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- syntax.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- table.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- terminal_theme.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- text.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- theme.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- themes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- traceback.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- tree.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _cell_widths.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _emoji_codes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _emoji_replace.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _export_format.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _extension.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _fileno.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _inspect.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _log_render.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _loop.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _null_file.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _palettes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _pick.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _ratio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _spinners.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _stack.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _timer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _win32_console.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _windows.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _windows_renderer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _wrap.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- abc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- align.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- ansi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- bar.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- box.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cells.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- color.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- color_triplet.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- columns.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- console.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- constrain.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- containers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- control.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- default_styles.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- diagnose.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- emoji.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- file_proxy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- filesize.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- highlighter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- jupyter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- layout.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- live.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- live_render.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- logging.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- markup.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- measure.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- padding.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pager.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- palette.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- panel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pretty.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- progress.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- progress_bar.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- prompt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- protocol.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- region.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- repr.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- rule.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- scope.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- screen.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- segment.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- spinner.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- status.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- style.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- styled.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- syntax.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- table.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- terminal_theme.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- text.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- theme.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- themes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- traceback.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- tree.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tenacity/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _asyncio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- after.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- before.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- before_sleep.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- nap.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- retry.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- stop.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- tornadoweb.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wait.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _asyncio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- after.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- before.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- before_sleep.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- nap.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |   |-- retry.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- stop.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- tornadoweb.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- wait.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tomli/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _parser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _re.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- _types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _parser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _re.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |-- truststore/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _api.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _macos.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _openssl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _ssl_constants.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- _windows.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _api.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _macos.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _openssl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _ssl_constants.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _windows.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |-- urllib3/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _collections.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- connection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- connectionpool.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- fields.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- filepost.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- poolmanager.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- request.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- response.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- contrib/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- _appengine_environ.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- appengine.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- ntlmpool.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- pyopenssl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- securetransport.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- socks.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _securetransport/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |   |-- bindings.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |   \-- low_level.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |   |-- bindings.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |   \-- low_level.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- _appengine_environ.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- appengine.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- ntlmpool.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- pyopenssl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- securetransport.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- socks.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- packages/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- six.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- backports/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |   |-- makefile.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |   \-- weakref_finalize.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |   |-- makefile.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |   \-- weakref_finalize.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- six.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- util/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- connection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- proxy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- queue.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- request.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- response.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- retry.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- ssl_.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- ssl_match_hostname.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- ssltransport.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- timeout.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   |-- url.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |   \-- wait.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- connection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- proxy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- queue.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- request.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- response.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- retry.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- ssl_.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- ssl_match_hostname.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- ssltransport.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- timeout.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   |-- url.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |   \-- wait.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _collections.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- connection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- connectionpool.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- fields.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- filepost.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- poolmanager.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- request.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- response.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- webencodings/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- labels.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mklabels.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- tests.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- x_user_defined.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- labels.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mklabels.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- tests.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- x_user_defined.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- six.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- typing_extensions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- vendor.txt -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __pip-runner__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |-- pip-24.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- AUTHORS.txt -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- LICENSE.txt -> License or author text for an installed package.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- pkg_resources/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- _vendor/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- appdirs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- zipp.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- importlib_resources/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _adapters.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _itertools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _legacy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- abc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- readers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- simple.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _adapters.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _itertools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _legacy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- abc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- readers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- simple.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- jaraco/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- context.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- functools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- text/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- context.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- functools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- more_itertools/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- more.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- recipes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- more.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- recipes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- packaging/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __about__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _manylinux.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _musllinux.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _structures.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- markers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- requirements.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- specifiers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- tags.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __about__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _manylinux.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _musllinux.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _structures.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- markers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- requirements.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- specifiers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- tags.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pyparsing/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- actions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- helpers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- results.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- testing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- unicode.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- diagram/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- actions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- helpers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- results.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- testing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- unicode.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- appdirs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- zipp.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- extern/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- psycopg2/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _ipaddress.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _range.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- errorcodes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- extensions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- extras.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- pool.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- sql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- tz.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _ipaddress.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _psycopg.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |-- _range.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- errorcodes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- extensions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- extras.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- pool.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- sql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- tz.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- psycopg2_binary-2.9.11.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- DELVEWHEEL -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- psycopg2_binary.libs/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- libcrypto-3-x64-453e9f6331263f56ddbf269d2005e769.dll -> Native binary for an installed package.
|   |       |   |-- libpq-634d1dba4506d02f8e5f3384e9a4e276.dll -> Native binary for an installed package.
|   |       |   \-- libssl-3-x64-bba7a3010309a8b91169249a596c3da2.dll -> Native binary for an installed package.
|   |       |-- pyasn1/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- debug.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- error.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- codec/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- streaming.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ber/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- decoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- encoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- eoo.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- decoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- encoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- eoo.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cer/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- decoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- encoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- decoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- encoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- der/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- decoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- encoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- decoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- encoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- native/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- decoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- encoder.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- decoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- encoder.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- streaming.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- compat/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- integer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- integer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- type/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- char.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- constraint.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- error.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- namedtype.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- namedval.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- opentype.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- tag.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- tagmap.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- univ.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- useful.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- char.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- constraint.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- error.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- namedtype.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- namedval.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- opentype.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tag.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tagmap.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- univ.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- useful.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- debug.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- error.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- pyasn1-0.6.2.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE.rst -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   |-- WHEEL -> Installed-package metadata file.
|   |       |   \-- zip-safe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |-- pycparser/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _ast_gen.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- ast_transforms.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- c_ast.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- c_generator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- c_lexer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- c_parser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _ast_gen.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _c_ast.cfg -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- ast_transforms.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- c_ast.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- c_generator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- c_lexer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- c_parser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- pycparser-3.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- pydantic/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _migration.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- alias_generators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- aliases.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- annotated_handlers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- class_validators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- color.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- dataclasses.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- datetime_parse.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- decorator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- env_settings.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- error_wrappers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- fields.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- functional_serializers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- functional_validators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- generics.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- json_schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- main.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- mypy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- networks.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- parse.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- root_model.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- tools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- type_adapter.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- typing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- validate_call_decorator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- validators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- warnings.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- _internal/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _core_metadata.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _core_utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _dataclasses.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _decorators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _decorators_v1.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _discriminated_union.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _docs_extraction.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _fields.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _forward_ref.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _generate_schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _generics.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _git.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _import_utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _internal_dataclass.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _known_annotated_metadata.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _mock_val_ser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _model_construction.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _namespace_utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _repr.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _schema_gather.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _schema_generation_shared.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _serializers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _signature.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _typing_extra.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _validate_call.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- _validators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _core_metadata.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _core_utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _dataclasses.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _decorators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _decorators_v1.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _discriminated_union.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _docs_extraction.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _fields.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _forward_ref.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _generate_schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _generics.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _git.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _import_utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _internal_dataclass.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _known_annotated_metadata.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _mock_val_ser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _model_construction.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _namespace_utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _repr.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _schema_gather.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _schema_generation_shared.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _serializers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _signature.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _typing_extra.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _validate_call.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- _validators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- deprecated/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- class_validators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- copy_internals.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- decorator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- parse.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- tools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- class_validators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- copy_internals.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- decorator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- parse.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- tools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- experimental/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- arguments_schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- missing_sentinel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- pipeline.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- arguments_schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- missing_sentinel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- pipeline.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- plugin/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _loader.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- _schema_validator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _loader.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- _schema_validator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- v1/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _hypothesis_plugin.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- annotated_types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- class_validators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- color.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dataclasses.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- datetime_parse.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- decorator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- env_settings.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- error_wrappers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fields.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- generics.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- main.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mypy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- networks.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- parse.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- tools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- typing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- validators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _hypothesis_plugin.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- annotated_types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- class_validators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- color.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dataclasses.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- datetime_parse.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- decorator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- env_settings.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- error_wrappers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fields.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- generics.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- main.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mypy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- networks.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- parse.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |   |-- schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- typing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- validators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _migration.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- alias_generators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- aliases.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- annotated_handlers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- class_validators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- color.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- dataclasses.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- datetime_parse.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- decorator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- env_settings.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- error_wrappers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- fields.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- functional_serializers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- functional_validators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- generics.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- json_schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- main.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- mypy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- networks.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- parse.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- root_model.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- tools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- type_adapter.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- typing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- validate_call_decorator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- validators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- warnings.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- pydantic-2.12.5.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- pydantic_core/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- core_schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _pydantic_core.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |-- _pydantic_core.pyi -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- core_schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |-- pydantic_core-2.41.5.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- python_dotenv-1.2.2.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- python_jose-3.5.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- rsa/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- asn1.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- cli.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- key.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- parallel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- pem.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- pkcs1.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- pkcs1_v2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- prime.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- randnum.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- transform.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- asn1.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- cli.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- key.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- parallel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- pem.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- pkcs1.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- pkcs1_v2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- prime.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- randnum.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- transform.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- rsa-4.9.1.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- LICENSE -> License or author text for an installed package.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- setuptools/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _deprecation_warning.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _entry_points.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _imp.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _importlib.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _itertools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _path.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _reqs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- archive_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- build_meta.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- dep_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- depends.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- discovery.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- dist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- extension.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- glob.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- installer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- launch.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- logging.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- monkey.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- msvc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- namespaces.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- package_index.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- py34compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- sandbox.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- unicode_utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- windows_support.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- _distutils/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _collections.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _functools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _macos_compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _msvccompiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- archive_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- bcppcompiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ccompiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cmd.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cygwinccompiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- debug.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dep_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dir_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- extension.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- fancy_getopt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- file_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- filelist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- log.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- msvc9compiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- msvccompiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- py38compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- py39compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- spawn.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sysconfig.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- text_file.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- unixccompiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- versionpredicate.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- command/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _framework_compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- bdist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- bdist_dumb.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- bdist_rpm.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- build.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- build_clib.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- build_ext.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- build_py.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- build_scripts.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- check.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- clean.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- install.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- install_data.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- install_egg_info.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- install_headers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- install_lib.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- install_scripts.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- py37compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- register.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- sdist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- upload.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _framework_compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- bdist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- bdist_dumb.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- bdist_rpm.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- build.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- build_clib.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- build_ext.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- build_py.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- build_scripts.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- check.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- clean.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install_data.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install_egg_info.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install_headers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install_lib.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- install_scripts.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- py37compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- register.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- sdist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- upload.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _collections.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _functools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _macos_compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _msvccompiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- archive_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- bcppcompiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ccompiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cmd.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cygwinccompiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- debug.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dep_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dir_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- extension.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- fancy_getopt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- file_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- filelist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- log.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- msvc9compiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- msvccompiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- py38compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- py39compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- spawn.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sysconfig.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- text_file.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- unixccompiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- versionpredicate.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _vendor/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ordered_set.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- typing_extensions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- zipp.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- importlib_metadata/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _adapters.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _collections.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _functools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _itertools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _meta.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- _text.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _adapters.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _collections.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _functools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _itertools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _meta.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- _text.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- importlib_resources/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _adapters.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _itertools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _legacy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- abc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- readers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- simple.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _adapters.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _itertools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _legacy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- abc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- readers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- simple.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- jaraco/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- context.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- functools.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- text/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- context.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- functools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- more_itertools/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- more.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- recipes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- more.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- recipes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- packaging/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __about__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _manylinux.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _musllinux.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _structures.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- markers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- requirements.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- specifiers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- tags.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- version.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __about__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _manylinux.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _musllinux.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _structures.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- markers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- requirements.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- specifiers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- tags.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pyparsing/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- actions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- core.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- helpers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- results.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- testing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- unicode.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- diagram/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- actions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- core.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- helpers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- results.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- testing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- unicode.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tomli/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _parser.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _re.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- _types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _parser.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _re.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- _types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ordered_set.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- typing_extensions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- zipp.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- command/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- alias.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- bdist_egg.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- bdist_rpm.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- build.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- build_clib.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- build_ext.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- build_py.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- develop.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dist_info.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- easy_install.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- editable_wheel.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- egg_info.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- install.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- install_egg_info.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- install_lib.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- install_scripts.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- py36compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- register.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- rotate.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- saveopts.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sdist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- setopt.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- test.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- upload.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- upload_docs.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- alias.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- bdist_egg.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- bdist_rpm.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- build.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- build_clib.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- build_ext.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- build_py.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- develop.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dist_info.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- easy_install.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- editable_wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- egg_info.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- install.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- install_egg_info.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- install_lib.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- install_scripts.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- launcher manifest.xml -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- py36compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- register.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- rotate.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- saveopts.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sdist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- setopt.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- test.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- upload.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- upload_docs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- config/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _apply_pyprojecttoml.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- expand.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- pyprojecttoml.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- setupcfg.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _validate_pyproject/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- error_reporting.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- extra_validations.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- fastjsonschema_exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- fastjsonschema_validations.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- formats.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- error_reporting.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- extra_validations.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- fastjsonschema_exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- fastjsonschema_validations.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- formats.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _apply_pyprojecttoml.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- expand.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pyprojecttoml.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- setupcfg.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- extern/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _deprecation_warning.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _entry_points.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _imp.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _importlib.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _itertools.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _path.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _reqs.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- archive_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- build_meta.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- cli-32.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- cli-64.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- cli-arm64.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- cli.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- dep_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- depends.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- discovery.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- dist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- extension.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- glob.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- gui-32.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- gui-64.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- gui-arm64.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- gui.exe -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- installer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- launch.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- logging.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- monkey.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- msvc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- namespaces.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- package_index.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py34compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- sandbox.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- script (dev).tmpl -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- script.tmpl -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- unicode_utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- version.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- wheel.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- windows_support.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- setuptools-65.5.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- LICENSE -> License or author text for an installed package.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- six-1.17.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- LICENSE -> License or author text for an installed package.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- sqlalchemy/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- events.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- inspection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- log.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- connectors/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- aioodbc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- asyncio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- pyodbc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- aioodbc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- asyncio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- pyodbc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- cyextension/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   \-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- collections.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |   |-- collections.pyx -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- immutabledict.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |   |-- immutabledict.pxd -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- immutabledict.pyx -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- processors.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |   |-- processors.pyx -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- resultproxy.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |   |-- resultproxy.pyx -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |   |-- util.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |   |   \-- util.pyx -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- dialects/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- _typing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- mssql/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- aioodbc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- information_schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- provision.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pymssql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- pyodbc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- aioodbc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- information_schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- provision.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pymssql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- pyodbc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mysql/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- aiomysql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- asyncmy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cymysql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- dml.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- enumerated.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- expression.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mariadb.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mariadbconnector.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mysqlconnector.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mysqldb.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- provision.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pymysql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pyodbc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- reflection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- reserved_words.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- aiomysql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- asyncmy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cymysql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- dml.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- enumerated.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- expression.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mariadb.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mariadbconnector.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mysqlconnector.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mysqldb.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- provision.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pymysql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pyodbc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- reflection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- reserved_words.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- oracle/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- cx_oracle.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- dictionary.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- oracledb.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- provision.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- vector.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- cx_oracle.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- dictionary.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- oracledb.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- provision.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- vector.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- postgresql/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- _psycopg_common.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- array.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- asyncpg.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- dml.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- ext.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- hstore.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- named_types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- operators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pg8000.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pg_catalog.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- provision.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- psycopg.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- psycopg2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- psycopg2cffi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- ranges.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- _psycopg_common.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- array.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- asyncpg.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- dml.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- ext.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- hstore.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- named_types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- operators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pg8000.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pg_catalog.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- provision.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- psycopg.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- psycopg2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- psycopg2cffi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- ranges.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sqlite/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- aiosqlite.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- dml.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- json.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- provision.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- pysqlcipher.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- pysqlite.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- aiosqlite.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- dml.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- json.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- provision.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- pysqlcipher.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- pysqlite.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _typing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- type_migration_guidelines.txt -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |   |-- engine/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _py_processors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _py_row.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _py_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- characteristics.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- create.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cursor.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- default.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- events.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- interfaces.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mock.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- processors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- reflection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- result.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- row.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- strategies.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- url.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _py_processors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _py_row.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _py_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- characteristics.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- create.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cursor.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- default.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- events.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- interfaces.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mock.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- processors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- reflection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- result.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- row.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- strategies.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- url.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- event/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- api.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- attr.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- legacy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- registry.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- api.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- attr.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- legacy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- registry.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- ext/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- associationproxy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- automap.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- baked.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- compiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- horizontal_shard.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- hybrid.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- indexable.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- instrumentation.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mutable.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- orderinglist.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- serializer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- asyncio/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- engine.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- exc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- result.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- scoping.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- session.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- engine.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- exc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- result.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- scoping.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- session.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- declarative/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- extensions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- extensions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mypy/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- apply.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- decl_class.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- infer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- names.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- plugin.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- apply.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- decl_class.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- infer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- names.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- plugin.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- associationproxy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- automap.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- baked.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- compiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- horizontal_shard.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- hybrid.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- indexable.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- instrumentation.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mutable.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- orderinglist.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- serializer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- future/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- engine.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- engine.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- orm/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _orm_constructors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _typing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- attributes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- bulk_persistence.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- clsregistry.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- collections.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- context.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- decl_api.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- decl_base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dependency.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- descriptor_props.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dynamic.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- evaluator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- events.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- exc.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- identity.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- instrumentation.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- interfaces.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- loading.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mapped_collection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- mapper.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- path_registry.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- persistence.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- properties.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- query.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- relationships.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- scoping.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- session.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- state.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- state_changes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- strategies.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- strategy_options.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sync.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- unitofwork.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- writeonly.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _orm_constructors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _typing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- attributes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- bulk_persistence.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- clsregistry.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- collections.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- context.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- decl_api.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- decl_base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dependency.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- descriptor_props.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dynamic.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- evaluator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- events.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- exc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- identity.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- instrumentation.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- interfaces.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- loading.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mapped_collection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- mapper.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- path_registry.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- persistence.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- properties.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- query.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- relationships.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- scoping.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- session.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- state.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- state_changes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- strategies.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- strategy_options.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sync.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- unitofwork.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- writeonly.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- pool/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- events.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- events.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- sql/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _dml_constructors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _elements_constructors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _orm_types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _py_util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _selectable_constructors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _typing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- annotation.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cache_key.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- coercions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- compiler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- crud.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- ddl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- default_comparator.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- dml.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- elements.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- events.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- expression.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- functions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- lambdas.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- naming.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- operators.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- roles.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- selectable.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sqltypes.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- traversals.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- type_api.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- visitors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _dml_constructors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _elements_constructors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _orm_types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _py_util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _selectable_constructors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _typing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- annotation.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cache_key.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- coercions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- compiler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- crud.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- ddl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- default_comparator.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- dml.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- elements.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- events.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- expression.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- functions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- lambdas.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- naming.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- operators.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- roles.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- selectable.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sqltypes.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- traversals.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- type_api.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- visitors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- testing/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- assertions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- assertsql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- asyncio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- engines.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- entities.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- exclusions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- pickleable.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- profiling.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- provision.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- requirements.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- schema.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- util.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- warnings.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- fixtures/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- mypy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- orm.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- sql.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- mypy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- orm.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- sql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- plugin/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- bootstrap.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- plugin_base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- pytestplugin.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- bootstrap.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- plugin_base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- pytestplugin.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- suite/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_cte.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_ddl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_deprecations.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_dialect.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_insert.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_reflection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_results.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_rowcount.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_select.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_sequence.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- test_unicode_ddl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- test_update_delete.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_cte.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_ddl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_deprecations.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_dialect.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_insert.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_reflection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_results.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_rowcount.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_select.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_sequence.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- test_unicode_ddl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- test_update_delete.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- assertions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- assertsql.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- asyncio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- engines.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- entities.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- exclusions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- pickleable.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- profiling.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- provision.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- requirements.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- util.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- warnings.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- util/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _collections.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _concurrency_py3k.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _has_cy.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- _py_collections.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- concurrency.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- deprecations.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- langhelpers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- preloaded.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- queue.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- tool_support.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- topological.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- typing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _collections.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _concurrency_py3k.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _has_cy.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- _py_collections.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- concurrency.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- deprecations.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- langhelpers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- preloaded.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- queue.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- tool_support.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- topological.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- typing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- events.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exc.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- inspection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- log.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- schema.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- sqlalchemy-2.0.48.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   |-- top_level.txt -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- starlette/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _exception_handler.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- applications.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- authentication.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- background.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- concurrency.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- convertors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- datastructures.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- endpoints.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- formparsers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- requests.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- responses.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- routing.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- schemas.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- staticfiles.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- status.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- templating.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- testclient.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- websockets.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- middleware/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- authentication.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- base.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- cors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- errors.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- exceptions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- gzip.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- httpsredirect.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- sessions.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- trustedhost.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- wsgi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- authentication.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- base.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- cors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- errors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- gzip.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- httpsredirect.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- sessions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- trustedhost.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- wsgi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _exception_handler.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- applications.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- authentication.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- background.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- concurrency.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- convertors.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- datastructures.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- endpoints.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- exceptions.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- formparsers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- requests.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- responses.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- routing.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- schemas.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- staticfiles.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- status.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- templating.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- testclient.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- websockets.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- starlette-0.52.1.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE.md -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- typing_extensions-4.15.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- typing_inspection/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- introspection.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- typing_objects.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- introspection.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- typing_objects.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- typing_objects.pyi -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |-- typing_inspection-0.4.2.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE -> License or author text for an installed package.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- uvicorn/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __main__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _compat.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _subprocess.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- _types.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- importer.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- logging.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- main.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- server.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   \-- workers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |-- lifespan/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- off.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- on.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- off.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- on.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- loops/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- asyncio.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- auto.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- uvloop.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- asyncio.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- auto.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- uvloop.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- middleware/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- asgi2.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- message_logger.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- proxy_headers.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- wsgi.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- asgi2.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- message_logger.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- proxy_headers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- wsgi.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- protocols/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- utils.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- http/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- auto.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- flow_control.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- h11_impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- httptools_impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- auto.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- flow_control.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- h11_impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- httptools_impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- websockets/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- auto.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- websockets_impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   |-- websockets_sansio_impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |   \-- wsproto_impl.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- auto.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- websockets_impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   |-- websockets_sansio_impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |   \-- wsproto_impl.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- utils.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- supervisors/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |       |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- basereload.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- multiprocess.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   |-- statreload.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |   \-- watchfilesreload.cpython-311.pyc -> Compiled bytecode cache for an installed package.
|   |       |   |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- basereload.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- multiprocess.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   |-- statreload.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |   \-- watchfilesreload.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __init__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- __main__.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _compat.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _subprocess.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- _types.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- config.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- importer.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- logging.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- main.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   |-- py.typed -> PEP 561 typing marker for an installed package.
|   |       |   |-- server.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |   \-- workers.py -> Third-party Python source inside the checked-in virtual environment.
|   |       |-- uvicorn-0.41.0.dist-info/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |-- licenses/ -> Subdirectory inside the checked-in virtual environment.
|   |       |   |   \-- LICENSE.md -> License or author text for an installed package.
|   |       |   |-- entry_points.txt -> Installed-package metadata file.
|   |       |   |-- INSTALLER -> Installed-package metadata file.
|   |       |   |-- METADATA -> Installed-package metadata file.
|   |       |   |-- RECORD -> Installed-package metadata file.
|   |       |   |-- REQUESTED -> Installed-package metadata file.
|   |       |   \-- WHEEL -> Installed-package metadata file.
|   |       |-- _cffi_backend.cp311-win_amd64.pyd -> Native binary for an installed package.
|   |       |-- distutils-precedence.pth -> File belonging to a checked-in third-party dependency inside the virtual environment.
|   |       |-- six.py -> Third-party Python source inside the checked-in virtual environment.
|   |       \-- typing_extensions.py -> Third-party Python source inside the checked-in virtual environment.
|   |-- Scripts/
|   |   |-- activate -> Virtual-environment activation or deactivation script.
|   |   |-- activate.bat -> Virtual-environment activation or deactivation script.
|   |   |-- Activate.ps1 -> Virtual-environment activation or deactivation script.
|   |   |-- deactivate.bat -> Virtual-environment activation or deactivation script.
|   |   |-- dotenv.exe -> Windows launcher executable for `dotenv` inside the virtual environment.
|   |   |-- email_validator.exe -> Windows launcher executable for `email_validator` inside the virtual environment.
|   |   |-- fastapi.exe -> Windows launcher executable for `fastapi` inside the virtual environment.
|   |   |-- pip.exe -> Windows launcher executable for `pip` inside the virtual environment.
|   |   |-- pip3.11.exe -> Windows launcher executable for `pip3.11` inside the virtual environment.
|   |   |-- pip3.exe -> Windows launcher executable for `pip3` inside the virtual environment.
|   |   |-- pyrsa-decrypt.exe -> Windows launcher executable for `pyrsa-decrypt` inside the virtual environment.
|   |   |-- pyrsa-encrypt.exe -> Windows launcher executable for `pyrsa-encrypt` inside the virtual environment.
|   |   |-- pyrsa-keygen.exe -> Windows launcher executable for `pyrsa-keygen` inside the virtual environment.
|   |   |-- pyrsa-priv2pub.exe -> Windows launcher executable for `pyrsa-priv2pub` inside the virtual environment.
|   |   |-- pyrsa-sign.exe -> Windows launcher executable for `pyrsa-sign` inside the virtual environment.
|   |   |-- pyrsa-verify.exe -> Windows launcher executable for `pyrsa-verify` inside the virtual environment.
|   |   |-- python.exe -> Windows launcher executable for `python` inside the virtual environment.
|   |   |-- pythonw.exe -> Windows launcher executable for `pythonw` inside the virtual environment.
|   |   \-- uvicorn.exe -> Windows launcher executable for `uvicorn` inside the virtual environment.
|   \-- pyvenv.cfg -> Virtual-environment configuration showing Python 3.11.9 and the base interpreter location.
|-- backend/ -> Backend source code, dependency manifest, and deployment config.
|   |-- app/
|   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for `__init__.py`.
|   |   |   |-- config.cpython-311.pyc -> Compiled bytecode cache for `config.py`.
|   |   |   |-- database.cpython-311.pyc -> Compiled bytecode cache for `database.py`.
|   |   |   \-- main.cpython-311.pyc -> Compiled bytecode cache for `main.py`.
|   |   |-- models/
|   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for `__init__.py`.
|   |   |   |   |-- checkin_form_model.cpython-311.pyc -> Compiled bytecode cache for `checkin_form_model.py`.
|   |   |   |   |-- checkin_model.cpython-311.pyc -> Compiled bytecode cache for `checkin_model.py`.
|   |   |   |   |-- event_model.cpython-311.pyc -> Compiled bytecode cache for `event_model.py`.
|   |   |   |   \-- user_model.cpython-311.pyc -> Compiled bytecode cache for `user_model.py`.
|   |   |   |-- __init__.py -> SQLAlchemy model module.
|   |   |   |-- checkin_form_model.py -> SQLAlchemy model module.
|   |   |   |-- checkin_model.py -> SQLAlchemy model module.
|   |   |   |-- event_model.py -> SQLAlchemy model module.
|   |   |   \-- user_model.py -> SQLAlchemy model module.
|   |   |-- routes/
|   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for `__init__.py`.
|   |   |   |   |-- admin_routes.cpython-311.pyc -> Compiled bytecode cache for `admin_routes.py`.
|   |   |   |   |-- auth_routes.cpython-311.pyc -> Compiled bytecode cache for `auth_routes.py`.
|   |   |   |   |-- builder_routes.cpython-311.pyc -> Compiled bytecode cache for `builder_routes.py`.
|   |   |   |   |-- checkin_routes.cpython-311.pyc -> Compiled bytecode cache for `checkin_routes.py`.
|   |   |   |   |-- events_routes.cpython-311.pyc -> Compiled bytecode cache for `events_routes.py`.
|   |   |   |   |-- form_routes.cpython-311.pyc -> Compiled bytecode cache for `form_routes.py`.
|   |   |   |   \-- launch_routes.cpython-311.pyc -> Compiled bytecode cache for `launch_routes.py`.
|   |   |   |-- __init__.py -> FastAPI route module.
|   |   |   |-- admin_routes.py -> FastAPI route module.
|   |   |   |-- auth_routes.py -> FastAPI route module.
|   |   |   |-- builder_routes.py -> FastAPI route module.
|   |   |   |-- checkin_routes.py -> FastAPI route module.
|   |   |   |-- events_routes.py -> FastAPI route module.
|   |   |   |-- form_routes.py -> FastAPI route module.
|   |   |   \-- launch_routes.py -> FastAPI route module.
|   |   |-- schemas/
|   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for `__init__.py`.
|   |   |   |   |-- checkin_form_schema.cpython-311.pyc -> Compiled bytecode cache for `checkin_form_schema.py`.
|   |   |   |   |-- checkin_schema.cpython-311.pyc -> Compiled bytecode cache for `checkin_schema.py`.
|   |   |   |   |-- event_schema.cpython-311.pyc -> Compiled bytecode cache for `event_schema.py`.
|   |   |   |   \-- user_schema.cpython-311.pyc -> Compiled bytecode cache for `user_schema.py`.
|   |   |   |-- __init__.py -> Pydantic schema module.
|   |   |   |-- checkin_form_schema.py -> Pydantic schema module.
|   |   |   |-- checkin_schema.py -> Pydantic schema module.
|   |   |   |-- event_schema.py -> Pydantic schema module.
|   |   |   \-- user_schema.py -> Pydantic schema module.
|   |   |-- services/
|   |   |   |-- __pycache__/ -> Generated Python bytecode cache.
|   |   |   |   |-- __init__.cpython-311.pyc -> Compiled bytecode cache for `__init__.py`.
|   |   |   |   |-- auth_service.cpython-311.pyc -> Compiled bytecode cache for `auth_service.py`.
|   |   |   |   \-- checkin_service.cpython-311.pyc -> Compiled bytecode cache for `checkin_service.py`.
|   |   |   |-- __init__.py -> Backend service/helper module.
|   |   |   |-- auth_service.py -> Backend service/helper module.
|   |   |   \-- checkin_service.py -> Backend service/helper module.
|   |   |-- __init__.py -> Backend Python module.
|   |   |-- config.py -> Backend Python module.
|   |   |-- database.py -> Backend Python module.
|   |   \-- main.py -> Backend Python module.
|   |-- render.yaml -> Render deployment manifest for the FastAPI backend service.
|   \-- requirements.txt -> Backend dependency manifest for the Python API.
|-- frontend/ -> Static frontend pages, shared fragments, and runtime assets.
|   |-- shared/ -> Reusable HTML fragments injected into public pages.
|   |   |-- footer.html -> Reusable HTML fragment.
|   |   \-- navbar.html -> Reusable HTML fragment.
|   |-- static/ -> Shared JavaScript runtime files and optional global CSS.
|   |   |-- config.js -> Shared frontend JavaScript helper.
|   |   |-- script.js -> Shared frontend JavaScript helper.
|   |   \-- styles.css -> Frontend stylesheet.
|   |-- admin-dashboard.html -> Static frontend page.
|   |-- builders.html -> Static frontend page.
|   |-- checkin.html -> Static frontend page.
|   |-- community.html -> Static frontend page.
|   |-- dashboard.html -> Static frontend page.
|   |-- events.html -> Static frontend page.
|   |-- home.html -> Static frontend page.
|   |-- launch-wall.html -> Static frontend page.
|   |-- login.html -> Static frontend page.
|   \-- vercel.json -> Vercel routing rule that maps the site root to home.html.
|-- .env -> Environment file with a Supabase PostgreSQL URL, JWT settings, and seeded admin credentials.
|-- .gitignore -> Ignore rules for the virtual environment, Python bytecode caches, and node_modules.
|-- AI_CONTEXT.md -> Machine-oriented repository context describing architecture, routes, data flow, and modification guidance.
|-- CODEBASE_OVERVIEW.md -> Generated repository overview document requested by the current task.
\-- README.md -> Human-readable setup, architecture, endpoint, and deployment guide for the project.

---

## 5. HOW EVERYTHING CONNECTS
The frontend is a set of static HTML pages that call the FastAPI backend over JSON REST endpoints using `fetch`. Public pages mostly load shared navbar/footer fragments from `frontend/shared/`, while authenticated pages either use the shared `apiFetch()` helper or define their own local wrapper around the same `window.API_BASE` value. After login, the browser stores the JWT in `localStorage`, and subsequent requests send it as a bearer token so FastAPI can resolve the current user with `HTTPBearer` and `python-jose`. Legacy cohort progress flows through the `checkins` table and powers `/builders` plus `/launch-wall`, while the newer scheduled-form workflow stores form definitions in `checkin_forms` and submissions in `form_responses`. SQLAlchemy models and sessions connect the route layer to PostgreSQL, and startup hooks create tables, ensure the `is_admin` column exists, and seed an admin user. Vercel is configured to serve the static frontend with `/` mapped to `home.html`, while Render is configured to run the backend as `uvicorn app.main:app`.

