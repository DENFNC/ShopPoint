from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from decimal import Decimal


class ProductBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = None
    price: Decimal = Field(..., gt=0, decimal_places=2)
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = None
    price: Optional[Decimal] = Field(None, gt=0, decimal_places=2)
    category: int


class ProductInDB(ProductBase):
    product_id: int
    created_at: datetime
    updated_at: datetime
    category: int

    model_config = ConfigDict(from_attributes=True)


class ProductImageResponse(BaseModel):
    image_url: HttpUrl
    model_config = ConfigDict(from_attributes=True)


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    images: List[ProductImageResponse] = Field(
        default_factory=list,
        alias="product_images"
    )

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
