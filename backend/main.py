from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.models import user_model, checkin_model, event_model
from app.models import checkin_form_model
from app.routes import (
    auth_routes,
    checkin_routes,
    builder_routes,
    launch_routes,
    admin_routes,
    events_routes,
    form_routes,
)
from app.services.config import settings
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import User
from app.services.auth_service import get_password_hash


def ensure_migrations():
    from sqlalchemy import text, inspect
    with engine.connect() as conn:
        inspector = inspect(engine)
        columns = [c["name"] for c in inspector.get_columns("users")]
        if "is_admin" not in columns:
            conn.execute(text("ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE"))
            conn.commit()


def seed_admin():
    db: Session = SessionLocal()
    try:
        admin = db.query(User).filter(User.email == settings.admin_email).first()
        if not admin:
            admin_user = User(
                name="Admin",
                email=settings.admin_email,
                password_hash=get_password_hash(settings.admin_password),
                project_name="Admin",
                cohort="Admin",
                is_admin=True
            )
            db.add(admin_user)
            db.commit()
    finally:
        db.close()


app = FastAPI(title="Start The Up API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    ensure_migrations()
    seed_admin()


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(auth_routes.router)
app.include_router(checkin_routes.router)
app.include_router(builder_routes.router)
app.include_router(launch_routes.router)
app.include_router(admin_routes.router)
app.include_router(events_routes.router)
app.include_router(form_routes.router)