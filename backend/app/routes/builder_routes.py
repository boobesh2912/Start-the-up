from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas.checkin_schema import BuilderStatus
from ..services import auth_service, checkin_service

router = APIRouter(tags=["builders"])


@router.get("/builders", response_model=List[BuilderStatus])
def get_builders(
    _: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    return checkin_service.get_builders(db)


@router.get("/checkins/builders", response_model=List[BuilderStatus])
def get_builders_alias(
    _: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    return checkin_service.get_builders(db)
