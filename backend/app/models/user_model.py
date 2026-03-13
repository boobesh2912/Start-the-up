from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    project_name = Column(String, nullable=False)
    cohort = Column(String, nullable=False, default="Cohort 1")
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
