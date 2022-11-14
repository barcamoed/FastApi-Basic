from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import enum
from enum import Enum


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int


class CourseCreate(CourseBase):
    ...
    # password: str


class Course(CourseBase):
    id: int
    # is_active: bool
    # created_at: datetime
    # updated_at: datetime

    class Config:
        orm_mode = True
