from datetime import datetime
from pydantic import BaseModel, ConfigDict


class WishlistItemBase(BaseModel):
    user_id: int
    product_id: int


class WishlistItemCreate(WishlistItemBase):
    pass


class WishlistItemInDB(WishlistItemBase):
    wishlist_item_id: int
    added_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class WishlistItemResponse(WishlistItemBase):
    wishlist_item_id: int
    added_at: datetime

    model_config = ConfigDict(from_attributes=True)
