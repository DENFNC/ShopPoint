from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import func, DECIMAL, ForeignKey
from datetime import datetime
from app.backend.db import Base


class OrderItem(Base):
    __tablename__ = 'order_items'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    order_id: Mapped[int] = mapped_column(
        ForeignKey('orders.id'),
        nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        nullable=False
    )
    quantity: Mapped[int] = mapped_column(
        nullable=False
    )
    unit_price: Mapped[float] = mapped_column(
        DECIMAL(10, 2),
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

    # Связь с Order
    order = relationship(
        "Order",
        back_populates="order_items"
    )
