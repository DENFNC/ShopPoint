import uuid

from urllib.parse import urlparse
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import UploadFile, HTTPException, status
from pathlib import Path


from app.core import FileValidator
from app.models import ProductImage
from app.config import settings
from app.backend import S3Storage


async def get_product_images_service(
    db: AsyncSession,
    product_id: int
):
    result = await db.scalars(
        select(ProductImage)
        .where(
            ProductImage.product_id == product_id
        )
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    result = result.all()
    return result


async def create_product_image_service(
    db: AsyncSession,
    validator: FileValidator,
    s3: S3Storage,
    file: UploadFile,
    product_id: int,
    alt_text: str,
    mimetype: str
):
    await validator.file_validate()
    change_name = f'{uuid.uuid4()}{Path(file.filename).suffix}'

    await s3.upload_object(
        body=file.file,
        bucket_name='product-images',
        key=f'public/{change_name}',
        content_type=mimetype
    )

    image = ProductImage(
        product_id=product_id,
        image_url=f'{settings.S3_PUBLIC_PRODUCTS_URL}/product-images/public/{change_name}',
        alt_text=alt_text
    )

    db.add(image)
    await db.commit()


async def get_product_image_service(
    db: AsyncSession,
    image_id: int
):
    result = await db.scalars(
        select(ProductImage)
        .where(
            ProductImage.id == image_id
        )
    )

    result = result.all()
    return result


async def update_product_image_service(
    db: AsyncSession,
    validator: FileValidator,
    file: UploadFile,
    s3: S3Storage,
    image_id: int,
    alt_text: str,
    mimetype: str
):
    await validator.file_validate()
    change_name = f'{uuid.uuid4()}{Path(file.filename).suffix}'

    await db.execute(
        update(ProductImage)
        .where(ProductImage.id == image_id)
        .values(
            image_url=f'{settings.S3_PUBLIC_PRODUCTS_URL}/product-images/public/{change_name}',
            alt_text=alt_text
        )
    )

    await db.commit()


async def delete_product_image_service(
    db: AsyncSession,
    image_id: str,
    s3: S3Storage
):
    await db.execute(
        delete(ProductImage)
        .where(
            ProductImage.id == image_id
        )
    )
