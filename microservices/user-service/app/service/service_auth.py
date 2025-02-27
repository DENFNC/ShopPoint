import asyncio
import bcrypt

from typing import Annotated
from fastapi import Body, Depends, HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


from app.core import UserVerification, JWTService
from app.config import settings
from app.schemas import UserCreate
from app.models import User


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


async def register_user_service(
    db: AsyncSession,
    create_user: UserCreate
):
    try:
        hash_password = bcrypt.hashpw(
            create_user.password.encode(),
            bcrypt.gensalt()
        )

        user = User(
            username=create_user.username,
            email=create_user.email,
            first_name=create_user.first_name,
            last_name=create_user.last_name,
            password=hash_password.decode('utf-8')
        )

        db.add(user)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='The user already exists'
        )


async def update_access_token_service(
    redis: Redis,
    service: JWTService,
    sid: str = Body(...)
):
    result = await redis.get(
        name=sid
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Ключ не найден'
        )

    access_token = service.create_access_token(
        sub=result,
        expire_time=settings.JWT_ACCESS_EXPIRES_TIME_DELTA
    )

    await redis.delete(
        sid
    )

    await redis.setex(
        name=service.create_session_id(),
        time=settings.JWT_REFRESH_EXPIRES_TIME_DELTA,
        value=result
    )

    return access_token
