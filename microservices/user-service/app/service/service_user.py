import bcrypt


from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy import update
from fastapi import HTTPException, status


from app.backend import AsyncSession
from app.models import User
from app.schemas import UserCreate, UserUpdate


async def get_active_users(db: AsyncSession):
    result = await db.scalars(
        select(User)
        .where(User.is_active)
    )

    users = result.all()

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Users not found"
        )

    return users


async def get_active_user(db: AsyncSession, user_id: int):
    user = await db.scalar(
        select(User)
        .where(
            User.id == user_id,
            User.is_active
        )
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


async def create_user_service(
    db: AsyncSession,
    create_user: UserCreate
):
    user = User(
        username=create_user.username,
        password=bcrypt.hashpw(create_user.password, bcrypt.gensalt()),
        email=create_user.email,
        first_name=create_user.first_name,
        last_name=create_user.last_name
    )

    db.add(user)
    await db.commit()


async def update_user_service(
    db: AsyncSession,
    user_id: int,
    update_user: UserUpdate
) -> None:
    await db.execute(
        update(User)
        .where(User.id == user_id)
        .values(
            username=update_user.username,
            email=update_user.email,
            first_name=update_user.first_name,
            last_name=update_user.last_name
        )
    )

    await db.commit()


async def delete_user_service(
    db: AsyncSession,
    user_id: int
):
    await db.execute(
        delete(User)
        .where(User.id == user_id)
    )

    await db.commit()
