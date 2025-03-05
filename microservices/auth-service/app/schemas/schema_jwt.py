from typing import List
from datetime import datetime
from pydantic import BaseModel


class BaseJWT(BaseModel):
    sub: str
    sid: str
    iat: int
    exp: int
    roles: List[str]


class RotationJWT(BaseModel):
    token: str


class SessionPayload(BaseModel):
    sub: str
    exp: datetime
