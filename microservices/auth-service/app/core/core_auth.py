import bcrypt

from fastapi import HTTPException
from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm


from app.models import AuthUser


class AuthManager:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def check_password(
        self,
        form_data: OAuth2PasswordRequestForm
    ):
        result = await self.db.scalar(
            select(AuthUser)
            .where(
                AuthUser.username == form_data.username
            )
        )

        if not result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        if not bcrypt.checkpw(form_data.password.encode(), result.password_hash.encode()):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        return result
