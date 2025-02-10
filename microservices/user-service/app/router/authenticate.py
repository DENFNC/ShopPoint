from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from redis.asyncio import Redis


from app.core import UserVerification, get_user_verification, get_jwt_service, JWTService
from app.service import authenticate_user_service
from app.backend import get_redis


router = APIRouter(prefix='/api/v1/auth', tags=['Auth'])


@router.post('/token')
async def authenticate_user(
    user_verification: Annotated[UserVerification, Depends(get_user_verification)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: Annotated[JWTService, Depends(get_jwt_service)],
    redis: Annotated[Redis, Depends(get_redis)]
):
    result = await authenticate_user_service(
        user_verification=user_verification,
        form_data=form_data,
        service=service,
        redis=redis
    )

    return result


@router.post('/refresh')
async def update_token(
    redis: Annotated[Redis, Depends(get_redis)]
):
    pass
