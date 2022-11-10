from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


