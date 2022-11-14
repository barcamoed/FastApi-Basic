import fastapi
from sqlalchemy.orm import Session
from db.db_setup import get_db
from fastapi import Depends, HTTPException
from typing import List
from pydantic_schema.course import Course, CourseCreate
from api.utils.courses import get_courses, get_course, create_course

router = fastapi.APIRouter()


@router.get('/courses', response_model=List[Course])
async def get_all_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.get('/fetch-course/{course_id}', response_model=Course)
async def get_this_course(course_id: int, db: Session = Depends(get_db)):
    course = get_course(db, course_id)
    return course


@router.post('/create-course', response_model=Course)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    course = create_course(db, course)
    return course


@router.delete('delete-course')
async def delete_course():
    return {"courses": []}
