from datetime import datetime

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    project_name: str
    cohort: str
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    project_name: str
    cohort: str = "Cohort 1"
    is_admin: bool = False


class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    password: str | None = None
    project_name: str
    cohort: str = "Cohort 1"
    is_admin: bool = False

    class Config:
        from_attributes = True
