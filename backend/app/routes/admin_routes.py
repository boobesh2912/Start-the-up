from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Checkin, Event, User
from ..schemas.event_schema import EventCreate, EventResponse, EventUpdate
from ..schemas.user_schema import CreateUserRequest, UserResponse, UserUpdate
from ..services import auth_service

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/users", response_model=UserResponse)
def create_user(
    body: CreateUserRequest,
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    existing = db.query(User).filter(User.email == body.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(
        name=body.name,
        email=body.email,
        password_hash=auth_service.hash_password(body.password),
        project_name=body.project_name,
        cohort=body.cohort,
        is_admin=body.is_admin,
        created_at=datetime.utcnow(),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/users", response_model=List[UserResponse])
def list_users(
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    return db.query(User).order_by(User.created_at.desc()).all()


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    body: UserUpdate,
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.email != body.email:
        if db.query(User).filter(User.email == body.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")

    user.name = body.name
    user.email = body.email
    if body.password:
        user.password_hash = auth_service.hash_password(body.password)
    user.project_name = body.project_name
    user.cohort = body.cohort
    user.is_admin = body.is_admin
    db.commit()
    db.refresh(user)
    return user


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.query(Checkin).filter(Checkin.user_id == user_id).delete()
    db.delete(user)
    db.commit()
    return {"status": "deleted"}


@router.post("/events", response_model=EventResponse)
def create_event(
    body: EventCreate,
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    event = Event(
        title=body.title,
        description=body.description,
        event_date=body.event_date,
        registration_link=str(body.registration_link) if body.registration_link else None,
        status=body.status,
        created_at=datetime.utcnow(),
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/events", response_model=List[EventResponse])
def list_events(
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    return db.query(Event).order_by(Event.event_date.asc()).all()


@router.put("/events/{event_id}", response_model=EventResponse)
def update_event(
    event_id: int,
    body: EventUpdate,
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    data = body.dict(exclude_unset=True)
    for key, value in data.items():
        if key == "registration_link" and value is not None:
            value = str(value)
        setattr(event, key, value)
    db.commit()
    db.refresh(event)
    return event


@router.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    _admin=Depends(auth_service.get_admin_user),
    db: Session = Depends(get_db),
):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"status": "deleted"}
