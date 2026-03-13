# Start The Up Builder Tracker

Full-stack builder tracker with FastAPI + Supabase PostgreSQL backend and a static HTML/Tailwind frontend.

**Features**
1. User login (JWT)
2. Check-in submissions
3. Builder progress board
4. Launch wall
5. Public community pages

**Tech Stack**
1. Backend: FastAPI, Supabase PostgreSQL, SQLAlchemy, Pydantic, JWT, bcrypt
2. Frontend: HTML, TailwindCSS, Vanilla JS
3. Deployment: Vercel (frontend), Render/Railway (backend)

**Repository Structure**
1. `backend/app/main.py`
2. `backend/app/config.py`
3. `backend/app/database.py`
4. `backend/app/models/`
5. `backend/app/schemas/`
6. `backend/app/routes/`
7. `backend/app/services/`
8. `backend/requirements.txt`
9. `frontend/*.html`
10. `frontend/static/script.js`
11. `.env`

---

## Environment Variables

Create `.env` in the project root:

```env
DATABASE_URL=postgresql://postgres:password@host:5432/postgres
JWT_SECRET=supersecretkey
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Optional (for admin seed):

```env
ADMIN_EMAIL=admin@starttheup.com
ADMIN_PASSWORD=admin123
```

---

## Local Development (VS Code)

1. Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

2. Connect to Supabase (or any PostgreSQL instance).

3. Run the backend:

```bash
cd backend
uvicorn app.main:app --reload
```

4. Open the frontend pages:

Open `frontend/home.html` in your browser (or use a static server).

---

## Frontend API Connection

`frontend/static/script.js` defines:

```js
const API_BASE = window.API_BASE || 'http://localhost:8000';
```

For production, set `window.API_BASE` before loading `script.js`, or update `API_BASE` to your deployed backend URL.

---

## API Endpoints

Primary endpoints:
1. `POST /login`
2. `GET /me`
3. `POST /checkin`
4. `GET /builders`
5. `GET /launch-wall`

Compatibility endpoints (kept to avoid breaking existing UI):
1. `GET /users/me`
2. `POST /checkins/`
3. `GET /checkins/me`
4. `GET /checkins/builders`
5. `GET /checkins/launch-wall`

---

## Database Tables

**users**
1. `id`
2. `name`
3. `email`
4. `password_hash`
5. `project_name`
6. `cohort`
7. `is_admin`
8. `created_at`

**checkins**
1. `id`
2. `user_id`
3. `update_text`
4. `demo_link`
5. `progress`
6. `blocker`
7. `created_at`

---

## Deployment

**Backend (Render/Railway)**
1. Set environment variables from `.env`
2. Start command:
   `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

**Frontend (Vercel)**
1. Set project root to `frontend/`
2. Update `API_BASE` to the backend URL

---

## Testing Checklist

1. User login works
2. Check-in submission works
3. Builder board loads data
4. Launch wall shows completed projects

---

## Supabase Connection

1. Create a Supabase project.
2. Open `Database` → `Settings`.
3. Copy the connection string.
4. Set it as `DATABASE_URL` in `.env`.

If your connection string starts with `postgres://`, it will be normalized automatically.
