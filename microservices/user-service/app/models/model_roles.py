from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, func, DateTime

from app.backend.db import Base


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    role_name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )

    user_roles = relationship(
        "UserRole",
        back_populates="role",
        cascade="all, delete-orphan"
    )
