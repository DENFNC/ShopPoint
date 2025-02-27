from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete


from app.models import Category
from app.schemas import CreateCategory
from app.schemas import UpdateCategory


async def get_categories_service(
    db: AsyncSession
):
    result = await db.scalars(
        select(Category)
    )

    categories = result.all()

    return categories


async def get_category_service(
    db: AsyncSession,
    category_id: int
):
    result = await db.scalars(
        select(Category)
        .where(
            Category.id == category_id
        )
    )

    category = result.all()

    return category


async def create_category_service(
    db: AsyncSession,
    create_category: CreateCategory
):
    category = Category(
        name=create_category.name,
        parent_category_id=create_category.parent_category_id
    )

    db.add(category)
    await db.commit()


async def update_category_service(
    db: AsyncSession,
    category_id: int,
    update_category: UpdateCategory
):
    await db.execute(
        update(Category)
        .where(
            Category.id == category_id
        )
        .values(
            name=update_category.name,
            parent_category_id=update_category.parent_category_id
        )
    )

    await db.commit()


async def delete_category_service(
    db: AsyncSession,
    category_id: int
):
    await db.execute(
        delete(Category)
        .where(
            Category.id == category_id
        )
    )

    await db.commit()
