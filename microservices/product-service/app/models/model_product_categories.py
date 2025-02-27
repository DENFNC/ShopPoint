from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, func

from app.backend import Base


class ProductCategory(Base):
    __tablename__ = 'product_categories'

    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id'),
        primary_key=True,
        nullable=False
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey('categories.id'),
        primary_key=True,
        nullable=False
    )
    assigned_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    product = relationship(
        "Product",
        back_populates="product_categories"
    )

    category = relationship(
        "Category",
        back_populates='product_categories'
    )
