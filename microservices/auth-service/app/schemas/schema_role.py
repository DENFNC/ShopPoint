from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from pydantic import ConfigDict


class RoleName(str, Enum):
    ADMIN: str = 'admin'
    USER: str = 'user'


class RoleBase(BaseModel):
    id: int
    role_name: RoleName
    created_at: datetime


class CreateRole(BaseModel):
    role_name: RoleName


class RoleInDB(RoleBase):
    model_config = ConfigDict(
        from_attributes=True
    )
