from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from pydantic import PositiveInt


class CategoryBase(BaseModel):
    name: str
    parent_category_id: Optional[PositiveInt] = 'null'


class CreateCategory(CategoryBase):
    pass


class CategoryInDB(CategoryBase):
    id: PositiveInt
    created_at: datetime
    updated_at: datetime
    is_active: bool


class UpdateCategory(CategoryBase):
    name: Optional[str] = None
    parent_category_id: Optional[PositiveInt] = 'null'
