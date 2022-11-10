import fastapi
from fastapi import Path, Query
from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):  # Using pydantic for validation of fields, It's like defining a type or interface in typescript
    email: str
    is_active: bool
    bio: Optional[str]  # If bio parameter is not in the request body, it will save it as null


users = []

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])  # response_model => to perform the field limiting and serialization
async def get_users():
    return users


@router.post("/create-user")
async def create_user(user: User):
    users.append(user)
    return users


@router.post("/fetch-user/{id}")
# Every path parameter (in the url like id here) must be defined inside the function like below
async def fetch_user(id: int = Path(..., description='User id to fetch user data', gt=0),
                     q: str = Query(None, max_length=5)):
    # dots (...) means required,
    # gt means greater than
    return {"user": users[id], "query": q}
