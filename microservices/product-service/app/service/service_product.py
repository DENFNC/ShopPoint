from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


from app.models import Product, ProductImage
from app.schemas import ProductCreate


async def get_products_service(
    db: AsyncSession
):
    result = select(Product).options(
        selectinload(Product.product_images).load_only(ProductImage.image_url)
    ).order_by(Product.id)

    return result


async def get_product_service(
    db: AsyncSession,
    product_id: int
):
    result = await db.scalars(
        select(Product)
        .where(
            Product.id == product_id
        )
    )

    product = result.one_or_none()

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return product


async def create_product_service(
    db: AsyncSession,
    create_product: ProductCreate
):
    product = Product(
        name=create_product.name,
        description=create_product.description,
        price=create_product.price,
    )

    product.product_categories

    db.add(product)
    await db.commit()


async def update_product_service(
    db: AsyncSession,
    update_product: ProductCreate,
    product_id: int
):
    await db.execute(
        update(Product)
        .where(
            Product.id == product_id
        )
        .values(
            name=update_product.name,
            description=update_product.description,
            price=update_product.price,
        )
    )

    await db.commit()


async def delete_product_service(
    db: AsyncSession,
    product_id: int
):
    await db.execute(
        update(Product)
        .where(
            Product.id == product_id
        )
        .values(
            is_active=False
        )
    )

    await db.commit()
