from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class CheckinForm(Base):
    __tablename__ = "checkin_forms"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    questions = Column(JSON, nullable=False)
    publish_at = Column(DateTime, nullable=False)
    close_at = Column(DateTime, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    responses = relationship("FormResponse", back_populates="form", cascade="all, delete-orphan")
    creator = relationship("User", foreign_keys=[created_by])


class FormResponse(Base):
    __tablename__ = "form_responses"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("checkin_forms.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    answers = Column(JSON, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)

    form = relationship("CheckinForm", back_populates="responses")
    user = relationship("User", foreign_keys=[user_id])