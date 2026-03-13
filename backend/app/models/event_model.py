from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from ..database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    event_date = Column(DateTime, nullable=False)
    registration_link = Column(String, nullable=True)
    status = Column(String, nullable=False, default="upcoming")
    created_at = Column(DateTime, default=datetime.utcnow)
