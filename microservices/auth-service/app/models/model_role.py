from datetime import datetime
from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from app.backend import Base
from app.models.model_auth_user_role import AuthUserRole


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True,
        index=True,
        nullable=False
    )
    role_name: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    user: Mapped[List['AuthUser']] = relationship(
        secondary=AuthUserRole.__table__,
        back_populates='role'
    )
