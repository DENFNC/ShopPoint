from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


from app.backend import Base


class AuthUserRole(Base):
    __tablename__ = 'auth_user_role'

    auth_user_id: Mapped[int] = mapped_column(
        ForeignKey('auth_users.id'),
        primary_key=True
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey('roles.id'),
        primary_key=True
    )
    assigned_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
