import bcrypt

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from sqlalchemy import select


from app.backend import AsyncSession
from app.models import User


class UserVerification:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def verify(
            self,
            form_data: OAuth2PasswordRequestForm
    ):
        user_data = await self.db.scalar(
            select(User)
            .where(
                User.username == form_data.username
            )
        )

        if user_data is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        if not bcrypt.checkpw(form_data.password.encode('utf-8'), user_data.password.encode('utf-8')):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        return user_data
