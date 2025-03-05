from datetime import datetime
from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from app.backend import Base
from app.models.model_auth_user_role import AuthUserRole


class AuthUser(Base):
    __tablename__ = 'auth_users'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True,
        index=True,
        nullable=False
    )
    username: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )
    password_hash: Mapped[str] = mapped_column(
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    role: Mapped[List['Role']] = relationship(
        secondary=AuthUserRole.__table__,
        back_populates='user',
    )
