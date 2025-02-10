from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Boolean, ForeignKey, String, func, DateTime, Date
from datetime import datetime, date

from app.backend.db import Base


class PaymentMethod(Base):
    __tablename__ = 'payment_methods'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )
    card_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    expiry_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    cardholder_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    billing_address: Mapped[str] = mapped_column(
        String(255),
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

    # Связь со стороны PaymentMethod к User (N -> 1)
    user = relationship(
        "User",
        back_populates="payment_methods"
    )
