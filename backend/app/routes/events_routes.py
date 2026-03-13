from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Event
from ..schemas.event_schema import EventResponse

router = APIRouter(tags=["events"])


@router.get("/events", response_model=List[EventResponse])
def get_upcoming_events(db: Session = Depends(get_db)):
    return (
        db.query(Event)
        .filter(Event.status == "upcoming")
        .order_by(Event.event_date.asc())
        .all()
    )
