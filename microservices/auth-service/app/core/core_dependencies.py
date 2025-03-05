from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.core_auth import AuthManager
from app.core.core_jwt import JWTCore, ManagerJWT
from app.backend import get_session
from app.schemas import RotationJWT


def get_auth(db: Annotated[AsyncSession, Depends(get_session)]) -> AuthManager:
    return AuthManager(db=db)


def get_jwt_core() -> JWTCore:
    return JWTCore()


def get_jwt_manager(jwt_core: Annotated[JWTCore, Depends(get_jwt_core)]) -> ManagerJWT:
    return ManagerJWT(jwt_core=jwt_core)


def get_current_username(
    jwt_core: Annotated[JWTCore, Depends(get_jwt_core)],
    jwt_token: RotationJWT
) -> str:
    token: dict = jwt_core.decode(jwt_token=jwt_token.token)
    username: str = token.get("sub")

    return username


def get_current_session_id(
    jwt_core: Annotated[JWTCore, Depends(get_jwt_core)],
    jwt_token: RotationJWT
) -> str:
    token: dict = jwt_core.decode(jwt_token=jwt_token.token)
    session_id: str = token.get('sid')

    return session_id
