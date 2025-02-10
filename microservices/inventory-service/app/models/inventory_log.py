from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import (
    Integer,
    String,
    DateTime,
    func,
    ForeignKey,
)
from datetime import datetime
from app.backend.db import Base


class InventoryLog(Base):
    __tablename__ = 'inventory_logs'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('inventory.product_id'),
        nullable=False
    )
    change_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    change_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )
    reason: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )

    # Связь с Inventory
    inventory = relationship(
        "Inventory",
        back_populates="logs"
    )
