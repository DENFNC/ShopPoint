from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from app.core.core_security import UserVerification
from app.core.core_jwt import JWTHandler, JWTService
from app.backend import AsyncSession, get_session
from app.models import User


async def get_current_username(
    db: AsyncSession,
    user_id: int
):
    result = await db.scalar(
        select(User.username)
        .where(
            User.id == user_id
        )
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return result


async def get_user_verification(db: Annotated[AsyncSession, Depends(get_session)]) -> UserVerification:
    return UserVerification(db=db)


async def get_jwt_handler() -> JWTHandler:
    return JWTHandler()


async def get_jwt_service() -> JWTService:
    return JWTService()
