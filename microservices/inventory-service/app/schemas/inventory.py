from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class InventoryBase(BaseModel):
    product_id: int = Field(...)
    current_quantity: int = Field(..., ge=0)

    model_config = ConfigDict(from_attributes=True)


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    current_quantity: Optional[int] = Field(None, ge=0)

    model_config = ConfigDict(from_attributes=True)


class InventoryInDB(InventoryBase):
    id: int
    created_at: datetime
    updated_at: datetime


class InventoryResponse(InventoryInDB):
    pass
