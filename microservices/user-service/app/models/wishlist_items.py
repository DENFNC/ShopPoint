from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Boolean, func, DateTime, ForeignKey
from datetime import datetime

from app.backend.db import Base


class WishlistItem(Base):
    __tablename__ = 'wishlist_items'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        nullable=False
    )
    added_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    user = relationship(
        'User',
        back_populates='wishlist_items'
    )
