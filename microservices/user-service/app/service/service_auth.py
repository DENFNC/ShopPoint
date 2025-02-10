import asyncio


from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from redis.asyncio import Redis


from app.core import UserVerification, get_user_verification, get_jwt_service, JWTService
from app.config import settings


async def authenticate_user_service(
    user_verification: UserVerification,
    form_data: OAuth2PasswordRequestForm,
    service: JWTService,
    redis: Redis
):
    semaphore = asyncio.Semaphore(10)

    result = await user_verification.verify(
        form_data=form_data
    )

    access_token = service.create_access_token(
        sub=result.username
    )

    async with semaphore:
        await redis.setex(
            name=service.create_session_id(),
            time=settings.JWT_REFRESH_EXPIRES_TIME_DELTA,
            value=form_data.username,
        )

    return access_token
