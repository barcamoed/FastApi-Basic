import fastapi
from fastapi import Request, Query
from api.utils.users import get_users, get_user_by_email, get_user, create_user
from typing import Optional, List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db
from pydantic_schema.user import UserCreate, User

# class User(BaseModel):  # Using pydantic for validation of fields, It's like defining a type or interface in typescript
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
async def create_new_user(request: Request, user: UserCreate, db: Session = Depends(get_db)):
    # print('user', user)
    # print('request', await request.json())
    return create_user(db=db, user=user)


@router.post("/fetch-user/{user_id}", response_model=User)
# Every path parameter (in the url like id here) must be defined inside the function like below
async def fetch_user(user_id: int, db: Session = Depends(get_db)):
    # dots (...) means required,
    # gt means greater than
    return get_user(db=db, user_id=user_id)
