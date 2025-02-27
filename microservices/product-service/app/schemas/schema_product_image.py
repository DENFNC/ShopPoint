from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class ProductImageBase(BaseModel):
    product_id: int
    alt_text: Optional[str] = Field(None, max_length=255)


class ProductImageCreate(ProductImageBase):
    pass


class ProductImageUpdate(BaseModel):
    image_url: Optional[HttpUrl] = None
    alt_text: Optional[str] = Field(None, max_length=255)
    product_id: Optional[int] = None


class ProductImageInDB(ProductImageBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductImageResponse(ProductImageBase):
    image_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
