from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas.user_schema import (
    CreateUserRequest,
    LoginRequest,
    TokenResponse,
    UserResponse,
)
from ..services import auth_service

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = auth_service.get_user_by_email(db, body.email)
    if not user or not auth_service.verify_password(body.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    token = auth_service.create_access_token({"sub": str(user.id)})
    return {"access_token": token}


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(auth_service.get_current_user)):
    return current_user


@router.get("/users/me", response_model=UserResponse)
def get_me_alias(current_user: User = Depends(auth_service.get_current_user)):
    return current_user


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
