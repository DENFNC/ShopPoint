from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ShippingAddressBase(BaseModel):
    user_id: int
    address_line1: str = Field(..., max_length=255)
    address_line2: Optional[str] = Field(None, max_length=255)
    city: str = Field(..., max_length=100)
    state: str = Field(..., max_length=100)
    zip_code: str = Field(..., max_length=20)
    country: str = Field(..., max_length=100)
    is_active: bool = True


class ShippingAddressCreate(ShippingAddressBase):
    pass


class ShippingAddressInDB(ShippingAddressBase):
    address_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ShippingAddressResponse(ShippingAddressBase):
    address_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
