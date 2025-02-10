from typing import Annotated, Dict, List, Sequence
from fastapi import APIRouter, Depends, status


from app.backend.db import AsyncSession
from app.backend.session import get_session
from app.models.users import User
from app.schemas.user import UserUpdate
from app.schemas.user import UserResponse
from app.service import get_active_users, get_active_user, update_user_service, delete_user_service


router = APIRouter(prefix='/api/v1/user', tags=['user'])


@router.get('/', status_code=status.HTTP_200_OK, response_model=Dict[str, List[UserResponse]])
async def get_users(
    db: Annotated[AsyncSession, Depends(get_session)]
) -> Dict[str, Sequence[User]]:

    users = await get_active_users(
        db=db
    )

    return {
        'Users': users
    }


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user(
    db: Annotated[AsyncSession, Depends(get_session)],
    user_id: int
) -> UserResponse:
    user = await get_active_user(
        db,
        user_id
    )

    return user


@router.put('/update/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user(
    db: Annotated[AsyncSession, Depends(get_session)],
    user_id: int,
    update_user: UserUpdate,
) -> None:
    await update_user_service(
        db=db,
        user_id=user_id,
        update_user=update_user
    )

    return None


@router.delete('/delete/{user_id}', status_code=status.HTTP_200_OK)
async def delete_user(
    db: Annotated[AsyncSession, Depends(get_session)],
    user_id: int
) -> None:
    await delete_user_service(
        db=db,
        user_id=user_id
    )

    return None
