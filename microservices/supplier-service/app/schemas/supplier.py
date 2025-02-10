from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class SupplierBase(BaseModel):
    name: str = Field(..., max_length=100)
    contact_email: EmailStr = Field(..., max_length=100)
    phone_number: str = Field(..., max_length=20)
    address: str = Field(..., max_length=255)
    is_active: bool = Field(default=True)

    model_config = ConfigDict(from_attributes=True)


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    contact_email: Optional[EmailStr] = Field(None, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=20)
    address: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = Field(None)

    model_config = ConfigDict(from_attributes=True)


class SupplierInDB(SupplierBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SupplierResponse(SupplierInDB):
    product_ids: List[int] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
