from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    unit_price: Decimal = Field(decimal_places=2, gt=0)

    model_config = ConfigDict(from_attributes=True)


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = Field(None, gt=0)
    unit_price: Optional[Decimal] = Field(None, decimal_places=2, gt=0)


class OrderItemInDB(OrderItemBase):
    order_item_id: int
    order_id: int
    created_at: datetime
    updated_at: datetime


class OrderItemResponse(OrderItemInDB):
    pass
