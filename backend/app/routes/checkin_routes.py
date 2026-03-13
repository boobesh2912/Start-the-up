from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas.checkin_schema import CheckinCreate, CheckinResponse
from ..services import auth_service, checkin_service

router = APIRouter(tags=["checkins"])


@router.post("/checkin", response_model=CheckinResponse)
def create_checkin(
    body: CheckinCreate,
    current_user: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    return checkin_service.create_checkin(db, current_user.id, body.dict())


@router.post("/checkins/", response_model=CheckinResponse)
def create_checkin_alias(
    body: CheckinCreate,
    current_user: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    return checkin_service.create_checkin(db, current_user.id, body.dict())


@router.get("/checkins/me", response_model=List[CheckinResponse])
def get_my_checkins(
    current_user: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    return checkin_service.get_user_checkins(db, current_user.id)
