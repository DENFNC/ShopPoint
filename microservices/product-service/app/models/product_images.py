from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, func, Text
from datetime import datetime

from app.backend.db import Base


class ProductImage(Base):
    __tablename__ = 'product_images'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id'),
        nullable=False
    )
    image_url: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    alt_text: Mapped[str] = mapped_column(
        Text,
        server_default=str(),
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    product = relationship(
        "Product",
        back_populates="product_images"
    )
