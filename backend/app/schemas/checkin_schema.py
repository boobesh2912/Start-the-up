from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CheckinCreate(BaseModel):
    update_text: str
    demo_link: Optional[str] = None
    progress: int
    blocker: Optional[str] = None


class CheckinResponse(BaseModel):
    id: int
    user_id: int
    update_text: str
    demo_link: Optional[str]
    progress: int
    blocker: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class BuilderStatus(BaseModel):
    id: int
    name: str
    project_name: str
    cohort: str
    progress: int
    last_update: Optional[datetime]
    demo_link: Optional[str]


class LaunchEntry(BaseModel):
    id: int
    name: str
    project_name: str
    demo_link: Optional[str]
    launched_at: Optional[datetime]

    class Config:
        from_attributes = True
