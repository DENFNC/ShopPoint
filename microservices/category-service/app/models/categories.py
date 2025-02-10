from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    func,
    UniqueConstraint,
    ForeignKey
)
from datetime import datetime
from app.backend.db import Base


class Category(Base):
    __tablename__ = 'categories'

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
    description: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    parent_category_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey('categories.id'),
        nullable=True
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
        UniqueConstraint('name', name='uq_category_name'),
    )

    # Самосвязь для родительской категории
    parent_category: Mapped['Category | None'] = relationship(
        "Category",
        remote_side=[id],
        backref="subcategories"
    )

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, name='{self.name}'), parent_category_id='{self.parent_category_id}'>"
