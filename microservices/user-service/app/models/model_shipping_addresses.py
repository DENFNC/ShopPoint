from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, func, DateTime, Boolean
from datetime import datetime

from app.backend.db import Base


class ShippingAddress(Base):
    __tablename__ = 'shipping_addresses'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )
    address_line1: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    address_line2: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    state: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    zip_code: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    # Связь со стороны адресов к пользователю
    user = relationship(
        "User",
        back_populates="shipping_addresses"
    )
