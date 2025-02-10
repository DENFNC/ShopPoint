import uuid
import jwt


from datetime import datetime, timedelta, timezone
from typing import Any, Dict
from jwt.exceptions import InvalidTokenError, InvalidSignatureError, ExpiredSignatureError, DecodeError
from fastapi import HTTPException, status


from app.config import settings
from app.schemas import AccessToken


class JWTHandler:
    def __init__(self):
        self._algorithm = settings.JWT_ALGORITHM
        self.__public_key = settings.public_key
        self.__private_key = settings.private_key

    @property
    def public_key(self):
        return self.__public_key

    @property
    def private_key(self):
        return self.__private_key

    def decode(self, jwt_token: str) -> Dict[str, Any]:
        try:
            jwt_decode = jwt.decode(
                jwt=jwt_token,
                key=self.public_key,
                algorithms=[self._algorithm],
            )
            return jwt_decode
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

    def encode(self, payload_data: Dict[str, Any]):
        jwt_encode = jwt.encode(
            payload=payload_data,
            algorithm=self._algorithm,
            key=self.private_key
        )

        return jwt_encode


class JWTService:
    def __init__(self):
        self.handler = JWTHandler()
        self.access_expire_time = settings.JWT_ACCESS_EXPIRES_TIME_DELTA
        self.session_id = str(uuid.uuid4())

    def create_access_token(
        self,
        sub: str,
        expire_time: int | None = None
    ):
        current_time = datetime.now(timezone.utc)
        expire_time = expire_time or self.access_expire_time
        expiration_time = current_time + timedelta(seconds=expire_time)

        validate_payload = AccessToken(
            sub=sub,
            sid=self.session_id,
            iat=int(current_time.timestamp()),
            exp=int(expiration_time.timestamp())
        )

        token = self.handler.encode(validate_payload.model_dump())

        return token

    def create_session_id(self):
        token_uuid = self.session_id

        return token_uuid
