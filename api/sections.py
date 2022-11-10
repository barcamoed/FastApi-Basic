import fastapi

router = fastapi.APIRouter()


@router.get('/sections')
async def get_courses():
    return {"sections": []}


@router.post('/create-section')
async def create_course():
    return {'sections': []}


@router.delete('delete-section')
async def delete_course():
    return {"sections": []}
