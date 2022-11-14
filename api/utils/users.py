from sqlalchemy.orm import Session
from fastapi import HTTPException

from db.models.user import User
from db.models.course import Course
from pydantic_schema.user import UserCreate


def get_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    else:
        return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_courses(db, user_id):
    user_courses = db.query(Course).filter(Course.user_id == user_id).all()
    return user_courses


def create_user(db: Session, user: UserCreate):
    user_exists = get_user_by_email(db, email=user.email)
    if user_exists:
        raise HTTPException(status_code=400, detail='User with this email already exists')
    else:
        db_user = User(email=user.email, role=user.role)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
