from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class RoleBase(BaseModel):
    role_name: str = Field(..., max_length=50)


class RoleCreate(RoleBase):
    pass


class RoleInDB(RoleBase):
    role_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RoleResponse(RoleBase):
    role_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
