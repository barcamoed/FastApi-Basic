import fastapi

router = fastapi.APIRouter()


@router.get('/courses')
async def get_courses():
    return {"courses": []}


@router.get('/course/:id')
async def get_course():
    return {"courses": []}


@router.post('/create-course')
async def create_course():
    return {'courses': []}


@router.delete('delete-course')
async def delete_course():
    return {"courses": []}
