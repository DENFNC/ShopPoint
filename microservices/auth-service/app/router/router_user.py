from typing import Annotated
from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis as AsyncRedis


from app.core import AuthManager
from app.core import get_auth
from app.core import ManagerJWT
from app.core import get_jwt_manager
from app.core import get_current_username
from app.core import get_current_session_id
from app.service import create_new_user_service
from app.service import get_users_service
from app.service import assign_role_to_user_service
from app.service import authentication_user_service
from app.service import get_user_service
from app.service import token_rotation_service
from app.schemas import UserCreate
from app.schemas import UserInDB
from app.schemas import CreateUserRole
from app.backend import get_session
from app.backend import get_redis


router = APIRouter(prefix='/api/v1/auth', tags=['Auth'])


@router.get('/users', response_model=List[UserInDB])
async def get_users(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    result = await get_users_service(
        db=db
    )

    return result


@router.get('/users/{auth_user_id}', response_model=UserInDB)
async def get_user(
    db: Annotated[AsyncSession, Depends(get_session)],
    user_id: int
):
    result = await get_user_service(
        db=db,
        user_id=user_id
    )

    return result


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_new_user(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_user: UserCreate
):
    result = await create_new_user_service(
        db=db,
        create_user=create_user
    )

    return result


@router.post('/login')
async def authentication_user(
    auth: Annotated[AuthManager, Depends(get_auth)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    manager_jwt: Annotated[ManagerJWT, Depends(get_jwt_manager)],
    redis_db: Annotated[AsyncRedis, Depends(get_redis)],
):
    result = await authentication_user_service(
        auth=auth,
        form_data=form_data,
        manager_jwt=manager_jwt,
        redis_db=redis_db,
    )

    return result


@router.post('/refresh')
async def refresh_token(
    redis_db: Annotated[AsyncRedis, Depends(get_redis)],
    manager_jwt: Annotated[ManagerJWT, Depends(get_jwt_manager)],
    username: Annotated[str, Depends(get_current_username)],
    session_id: Annotated[str, Depends(get_current_session_id)],
):
    result = await token_rotation_service(
        manager_jwt=manager_jwt,
        redis_db=redis_db,
        session_id=session_id,
        username=username,
    )

    return result


@router.post('/users/{user_id}/roles/{role_id}', status_code=status.HTTP_201_CREATED)
async def assign_role_to_user(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_user_role: CreateUserRole
):
    await assign_role_to_user_service(
        db=db,
        create_user_role=create_user_role
    )
