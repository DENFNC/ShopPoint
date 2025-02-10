from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, func, DateTime
from datetime import datetime

from app.backend.db import Base


class UserRole(Base):
    __tablename__ = 'user_roles'

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        primary_key=True
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey('roles.id'),
        primary_key=True
    )
    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )

    # Явные back_populates для избежания конфликтов
    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")
