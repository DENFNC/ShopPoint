from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseToken(BaseModel):
    iat: int
    exp: int


class AccessToken(BaseToken):
    sid: str
    sub: str
