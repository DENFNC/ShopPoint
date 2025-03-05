from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import PositiveInt
from pydantic import ConfigDict


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password_hash: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


class UserInDB(UserBase):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class CreateUserRole(BaseModel):
    user_id: int
    role_id: int
