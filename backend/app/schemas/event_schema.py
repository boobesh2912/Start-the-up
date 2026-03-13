from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class EventCreate(BaseModel):
    title: str
    description: str
    event_date: datetime
    registration_link: Optional[HttpUrl] = None
    status: str = "upcoming"


class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    event_date: Optional[datetime] = None
    registration_link: Optional[HttpUrl] = None
    status: Optional[str] = None


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    event_date: datetime
    registration_link: Optional[str]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
