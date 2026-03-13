from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas.checkin_schema import LaunchEntry
from ..services import auth_service, checkin_service

router = APIRouter(tags=["launch"])


@router.get("/launch-wall", response_model=List[LaunchEntry])
def get_launch_wall(
    _: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    return checkin_service.get_launch_wall(db)


@router.get("/checkins/launch-wall", response_model=List[LaunchEntry])
def get_launch_wall_alias(
    _: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db),
):
    return checkin_service.get_launch_wall(db)
