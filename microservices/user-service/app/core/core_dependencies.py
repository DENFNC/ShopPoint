from fastapi import HTTPException, status
from sqlalchemy import select


from app.backend import AsyncSession
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
