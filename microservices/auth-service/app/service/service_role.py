from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.models import Role
from app.schemas import CreateRole


async def get_roles_service(
    db: AsyncSession
):
    result = await db.scalars(
        select(Role)
    )

    return result.all()


async def get_role_service(
    db: AsyncSession,
    role_id: int
):
    result = await db.scalars(
        select(Role)
        .where(
            Role.id == role_id
        )
    )

    return result.first()


async def create_role_service(
    db: AsyncSession,
    create_role: CreateRole
):
    role = Role(
        role_name=create_role.role_name
    )

    db.add(role)
    await db.commit()
