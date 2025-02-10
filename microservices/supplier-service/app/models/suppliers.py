# app/backend/models.py

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    func,
    UniqueConstraint
)
from datetime import datetime
from app.backend.db import Base


class Supplier(Base):
    __tablename__ = 'suppliers'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )
    contact_email: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    phone_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False
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
        UniqueConstraint('name', name='uq_supplier_name'),
    )
