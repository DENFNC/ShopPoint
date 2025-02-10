from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class BaseReview(BaseModel):
    product_id: int
    user_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: str


class CreateReview(BaseReview):
    pass


class UpdateReview(BaseModel):
    rating: int
    comment: str


class DeleteReview(BaseReview):
    is_active: bool


class ReviewInDB(BaseReview):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
