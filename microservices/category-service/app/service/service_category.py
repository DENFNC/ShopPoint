from sqlalchemy import select, update
from fastapi import HTTPException, status
from loguru import logger


from app.backend import AsyncSession, get_session
from app.models import Category
from app.schemas import CategoryCreate


async def get_active_categories(
    db: AsyncSession
):
    result = await db.scalars(
        select(Category)
        .where(Category.is_active)
    )

    categories = result.all()

    logger.debug(f'{categories}')

    return categories


async def get_active_category(
    db: AsyncSession,
    category_id: int
):
    result = await db.scalars(
        select(Category)
        .where(
            Category.id == category_id,
            Category.is_active
        )
    )

    category = result.one_or_none()

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )

    return category


async def get_create_category(
    db: AsyncSession,
    create_category: CategoryCreate
):
    category = Category(
        name=create_category.name,
        description=create_category.description,
        parent_category_id=create_category.parent_category_id,
        is_active=create_category.is_active
    )

    db.add(category)
    await db.rollback()
