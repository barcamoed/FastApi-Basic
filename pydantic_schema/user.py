from pydantic import BaseModel
from datetime import datetime
import enum
from enum import Enum


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    ...
    # password: str


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
