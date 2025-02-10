from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.order_item import OrderItemCreate, OrderItemResponse


class OrderBase(BaseModel):
    user_id: int
    status: str = Field(..., max_length=50)
    total_amount: Decimal = Field(decimal_places=2, gt=0)
    shipping_address_id: int
    payment_method_id: int

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderUpdate(BaseModel):
    status: Optional[str] = Field(None, max_length=50)
    total_amount: Optional[Decimal] = Field(None, decimal_places=2, gt=0)
    shipping_address_id: Optional[int] = None
    payment_method_id: Optional[int] = None


class OrderInDB(OrderBase):
    order_id: int
    order_date: datetime
    created_at: datetime
    updated_at: datetime


class OrderResponse(OrderInDB):
    items: List[OrderItemResponse]
