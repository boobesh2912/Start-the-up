import os
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import text
from .database import Base, SessionLocal, engine
from .models import Checkin, User, Event
from .models.checkin_form_model import CheckinForm, FormResponse from .routes import ( admin_router, auth_router, builder_router, checkin_router, events_router, form_router, launch_router, )
from .services.auth_service import hash_password

app = FastAPI(title="Start The Up Builder Tracker", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(checkin_router)
app.include_router(builder_router)
app.include_router(launch_router)
app.include_router(admin_router)
app.include_router(form_router)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    ensure_migrations()
    seed_admin()


def seed_admin():
    db = SessionLocal()
    admin_email = os.getenv("ADMIN_EMAIL", "admin@starttheup.com")
    try:
        existing = db.query(User).filter(User.email == admin_email).first()
        if existing:
            return
        admin = User(
            name="Admin",
            email=admin_email,
            password_hash=hash_password(os.getenv("ADMIN_PASSWORD", "admin123")),
            project_name="Platform",
            cohort="Admin",
            is_admin=True,
            created_at=datetime.utcnow(),
        )
        db.add(admin)
        db.commit()
    finally:
        db.close()


def ensure_migrations():
    with engine.begin() as connection:
        connection.execute(
            text(
                "ALTER TABLE users "
                "ADD COLUMN IF NOT EXISTS is_admin BOOLEAN DEFAULT FALSE"
            )
        )
