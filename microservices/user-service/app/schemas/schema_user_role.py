from datetime import datetime
from pydantic import BaseModel, ConfigDict


class UserRoleBase(BaseModel):
    user_id: int
    role_id: int


class UserRoleCreate(UserRoleBase):
    pass


class UserRoleInDB(UserRoleBase):
    assigned_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserRoleResponse(UserRoleBase):
    assigned_at: datetime

    model_config = ConfigDict(from_attributes=True)
