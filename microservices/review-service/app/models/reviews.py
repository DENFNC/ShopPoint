from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import (
    Boolean,
    func,
    DateTime,
    Integer,
    Text,
    CheckConstraint
)
from datetime import datetime
from app.backend.db import Base


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    rating: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    __table_args__ = (
        CheckConstraint(
            'rating >= 1 AND rating <= 5',
            name='check_rating_range'
        ),
    )
