import fastapi
from fastapi import Request, Query
from api.utils.users import get_users, get_user_by_email, get_user_courses, get_user, create_user
from typing import Optional, List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic_schema.course import Course
from db.db_setup import get_db, async_get_db
from pydantic_schema.user import UserCreate, User

# Using pydantic for validation of fields, It's like defining a type or interface in typescript
# class User(BaseModel):
#     email: str
#     is_active: bool
#     bio: Optional[str]  # If bio parameter is not in the request body, it will save it as null
#
#
# users = []

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])  # response_model => to perform the field limiting and serialization
async def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 15):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/create-user", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    # print('user', user)
    # print('request', await request.json())
    return create_user(db=db, user=user)

    # Synchronous fetch user


# @router.post("/fetch-user/{user_id}", response_model=User)
# # Every path parameter (in the url like id here) must be defined inside the function like below
# async def fetch_user(user_id: int, db: Session = Depends(get_db)):
#     # dots (...) means required,
#     # gt means greater than
#     return get_user(db=db, user_id=user_id)


# ASynchronous fetch user
@router.post("/fetch-user/{user_id}", response_model=User)
# Every path parameter (in the url like id here) must be defined inside the function like below
async def fetch_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    # user = await get_user(db=db, user_id=user_id)
    return await get_user(db=db, user_id=user_id)


@router.get('/user-courses/{user_id}', response_model=List[Course])
async def fetch_user_courses(user_id: int, db: Session = Depends(get_db)):
    user_courses = get_user_courses(db, user_id)
    return user_courses
