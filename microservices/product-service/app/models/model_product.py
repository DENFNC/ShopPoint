from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, func, Text, DECIMAL, true
from datetime import datetime
from app.backend import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )
    price: Mapped[float] = mapped_column(
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
    is_active: Mapped[bool] = mapped_column(
        server_default=true(),
        nullable=False
    )

    product_images = relationship(
        "ProductImage",
        back_populates="product",
    )

    product_categories = relationship(
        "ProductCategory",
        secondary='product_categories',
        back_populates="product",
    )
