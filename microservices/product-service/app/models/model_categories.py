from datetime import datetime
from sqlalchemy import func, true
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from app.backend import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        index=True,
        primary_key=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )
    parent_category_id: Mapped[int] = mapped_column(
        server_default=None,
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
    is_active: Mapped[bool] = mapped_column(
        server_default=true(),
        nullable=False
    )

    product_categories = relationship(
        'ProductCategory',
        secondary='product_categories',
        back_populates='category'
    )
