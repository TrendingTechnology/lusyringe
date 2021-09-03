from fastapi import APIRouter

from .schemas.health_schema import HealthResponse

router = APIRouter(
    prefix="/health"
)


@router.get("", response_model=HealthResponse)
async def index():
    return {'ping': 'pong'}
