from sqlalchemy.orm import Session
from fastapi import HTTPException

from db.models.course import Course
from pydantic_schema.course import CourseCreate


def get_courses(db: Session):
    courses = db.query(Course).all()
    # if len(courses) <= 0:
    #     raise HTTPException(status_code=200, detail="empty array")
    # else:
    return courses


def get_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="course not found")
    else:
        return course


def create_course(db: Session, course: CourseCreate):
    course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course
