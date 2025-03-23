from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import (
    Integer,
    String,
    DateTime,
    func,
    ForeignKey,
    DECIMAL
)
from datetime import datetime
from app.backend.db import Base


class Inventory(Base):
    __tablename__ = 'inventory'

    product_id: Mapped[int] = mapped_column(
        primary_key=True,
        nullable=False
    )
    current_quantity: Mapped[int] = mapped_column(
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    # Связь с InventoryLog
    logs = relationship(
        "InventoryLog",
        back_populates="inventory",
        cascade="all, delete-orphan"
    )
