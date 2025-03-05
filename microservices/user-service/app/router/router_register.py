from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.backend import get_session
from app.service import register_user_service
from app.schemas import UserCreate

router = APIRouter(prefix='/api/v1/auth', tags=['Auth'])


@router.post('/register')
async def register(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_user: UserCreate
):
    await register_user_service(
        db=db,
        create_user=create_user
    )
