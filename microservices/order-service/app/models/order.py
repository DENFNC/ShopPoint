from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import (
    Boolean,
    String,
    func,
    DECIMAL,
    true
)
from datetime import datetime
from app.backend.db import Base


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        nullable=False
    )
    order_date: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    total_amount: Mapped[float] = mapped_column(
        DECIMAL(10, 2),
        nullable=False
    )
    shipping_address_id: Mapped[int] = mapped_column(
        nullable=False
    )
    payment_method_id: Mapped[int] = mapped_column(
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        server_default=true(),
        nullable=False
    )

    # Связь с OrderItem
    order_items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )
