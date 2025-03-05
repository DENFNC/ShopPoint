import bcrypt


from typing import List
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from redis.asyncio import Redis as AsyncRedis


from app.schemas import UserCreate
from app.schemas import SessionPayload
from app.schemas import CreateUserRole
from app.models import AuthUser
from app.models import AuthUserRole
from app.config import settings
from app.core import ManagerJWT
from app.core import AuthManager


def get_session_key(username: str, session_id: str) -> str:
    return f"session:{username}:{session_id}"


async def get_users_service(
    db: AsyncSession
):
    result = await db.scalars(
        select(AuthUser)
    )

    return result.all()


async def get_user_service(
    db: AsyncSession,
    user_id: int
):
    result = await db.scalars(
        select(AuthUser)
        .where(
            AuthUser.id == user_id
        )
    )

    return result.first()


async def create_new_user_service(
    db: AsyncSession,
    create_user: UserCreate
):
    try:
        result = AuthUser(
            username=create_user.username,
            email=create_user.email,
            password_hash=bcrypt.hashpw(
                create_user.password_hash.encode(),
                bcrypt.gensalt()
            ).decode('utf-8')
        )

        db.add(result)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT
        )
    except Exception:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


async def authentication_user_service(
    auth: AuthManager,
    form_data: OAuth2PasswordRequestForm,
    manager_jwt: ManagerJWT,
    redis_db: AsyncRedis,
) -> str:
    """
    Аутентификация пользователя, генерирует access token и сохраняет сессию в Redis.
    """
    await auth.check_password(form_data=form_data)
    datetime_exp = datetime.now(timezone.utc) + \
        timedelta(seconds=settings.JWT_REFRESH_EXPIRES_TIME_DELTA)

    access_token = manager_jwt.create_access_token(
        sub=form_data.username,
    )

    session_id = manager_jwt.create_session_id()
    session_key = get_session_key(form_data.username, session_id)

    value = SessionPayload(
        sub=form_data.username,
        exp=datetime_exp
    )

    await redis_db.setex(
        name=session_key,
        time=settings.JWT_REFRESH_EXPIRES_TIME_DELTA,
        value=value.model_dump_json()
    )

    return access_token


async def token_rotation_service(
    redis_db: AsyncRedis,
    manager_jwt: ManagerJWT,
    username: str,
    session_id: str
) -> str:
    new_session_id: str = manager_jwt.create_session_id()
    old_session_key: str = get_session_key(username, session_id)
    datetime_exp = datetime.now(timezone.utc) + \
        timedelta(seconds=settings.JWT_REFRESH_EXPIRES_TIME_DELTA)

    result = await redis_db.get(name=old_session_key)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid session or session expired"
        )

    new_session_key: str = get_session_key(username, new_session_id)

    access_token = manager_jwt.create_access_token(
        sub=username,
    )

    value = SessionPayload(
        sub=username,
        exp=datetime_exp
    )

    async with redis_db.pipeline() as pipe:
        pipe.delete(old_session_key)
        pipe.setex(
            name=new_session_key,
            time=settings.JWT_REFRESH_EXPIRES_TIME_DELTA,
            value=value.model_dump_json()
        )
        await pipe.execute()

    return access_token


async def assign_role_to_user_service(
    db: AsyncSession,
    create_user_role: CreateUserRole,
):
    try:
        user_role = AuthUserRole(
            auth_user_id=create_user_role.user_id,
            role_id=create_user_role.role_id
        )

        db.add(user_role)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='A database integrity constraint was violated. Please check your data.'
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
