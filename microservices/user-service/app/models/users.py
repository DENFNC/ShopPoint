from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Boolean, String, func, DateTime
from datetime import datetime

from app.backend.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
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

    # Связь 1 -> N: PaymentMethod
    payment_methods = relationship(
        "PaymentMethod",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    # Связь 1 -> N: ShippingAddress
    shipping_addresses = relationship(
        "ShippingAddress",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    wishlist_items = relationship(
        "WishlistItem",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    user_roles = relationship(
        "UserRole",
        back_populates="user",
        cascade="all, delete-orphan"
    )
