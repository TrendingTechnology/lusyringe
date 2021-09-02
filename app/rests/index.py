from fastapi import APIRouter

from .schemas.index_schema import IndexResponse

router = APIRouter(
    prefix="/hello"
)


@router.get("", response_model=IndexResponse)
async def index():
    return {'message': 'Hello, world!'}
