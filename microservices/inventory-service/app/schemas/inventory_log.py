from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class InventoryLogBase(BaseModel):
    product_id: int = Field(..., description="ID товара из ProductService")
    change_quantity: int = Field(
        ..., description="Изменение запасов (положительное или отрицательное)")
    reason: str = Field(..., max_length=255,
                        description='Причина (например, "Продажа", "Возврат")')

    model_config = ConfigDict(from_attributes=True)


class InventoryLogCreate(InventoryLogBase):
    pass


class InventoryLogInDB(InventoryLogBase):
    log_id: int
    change_date: datetime
    created_at: datetime


class InventoryLogResponse(InventoryLogInDB):
    pass
