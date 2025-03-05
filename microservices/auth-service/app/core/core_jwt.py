from datetime import datetime, timedelta, timezone
import uuid
import jwt

from fastapi import HTTPException
from fastapi import status
from typing import Dict
from typing import List
from typing import Any


from app.config import settings
from app.schemas import BaseJWT


class JWTCore:
    def __init__(self):
        self._algorithm = settings.ALGORITHM
        self._private_key = settings.private_key
        self._public_key = settings.public_key

    def decode(
        self,
        jwt_token: str
    ):
        try:
            result = jwt.decode(
                jwt=jwt_token,
                key=self._public_key,
                algorithms=[self._algorithm]
            )
            return result
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        except jwt.InvalidSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        except jwt.InvalidTokenError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY
            )

    def encode(self, payload: Dict[str, str]):
        result = jwt.encode(
            payload=payload,
            key=self._private_key,
            algorithm=self._algorithm
        )

        return result


class ManagerJWT:
    def __init__(self, jwt_core: JWTCore):
        self.core = jwt_core
        self.access_time_delta = settings.JWT_ACCESS_EXPIRES_TIME_DELTA
        self.session_id = str(uuid.uuid4())

    def create_access_token(
        self,
        sub: str,
        expire_time: int | None = None
    ):
        current_time = datetime.now(timezone.utc)
        expire_time = expire_time or settings.JWT_ACCESS_EXPIRES_TIME_DELTA
        expiration_time = current_time + timedelta(seconds=expire_time)

        validate_payload = BaseJWT(
            sub=sub,
            sid=self.session_id,
            iat=int(current_time.timestamp()),
            exp=int(expiration_time.timestamp()),
        )

        token = self.core.encode(validate_payload.model_dump())

        return token

    def create_session_id(self):
        return self.session_id
