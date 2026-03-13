from pydantic import BaseModel
from typing import List, Optional, Any, Dict
from datetime import datetime


class QuestionSchema(BaseModel):
    id: str
    text: str
    type: str  # "text", "textarea", "number", "select"
    required: bool = True
    options: Optional[List[str]] = None


class CheckinFormCreate(BaseModel):
    title: str
    description: Optional[str] = None
    questions: List[QuestionSchema]
    publish_at: datetime
    # close_at auto-set to publish_at + 24h on backend


class CheckinFormUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    questions: Optional[List[QuestionSchema]] = None
    publish_at: Optional[datetime] = None


class CheckinFormResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    questions: List[Dict[str, Any]]
    publish_at: datetime
    close_at: datetime
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True


class FormResponseCreate(BaseModel):
    answers: Dict[str, Any]


class FormResponseOut(BaseModel):
    id: int
    form_id: int
    user_id: int
    answers: Dict[str, Any]
    submitted_at: datetime

    class Config:
        from_attributes = True


class FormResponseWithUser(FormResponseOut):
    user_name: Optional[str] = None
    user_email: Optional[str] = None
    project_name: Optional[str] = None