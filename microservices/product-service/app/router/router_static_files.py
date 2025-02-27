from typing import Annotated
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession


from app.core import FileValidator, get_file_validator, get_s3, get_mimetype_file
from app.service import get_product_images_service, get_product_image_service, create_product_image_service, update_product_image_service
from app.backend import get_session, S3Storage
# from app.schemas import ProductImageCreate


router = APIRouter(prefix='/api/v1/products', tags=['Static'])


@router.get('/{product_id}/images')
async def get_product_images(
    db: Annotated[AsyncSession, Depends(get_session)],
    product_id: int
):
    images = await get_product_images_service(
        db=db,
        product_id=product_id
    )

    return images


@router.get('/{product_id}/images/{image_id}')
async def get_product_image(
    db: Annotated[AsyncSession, Depends(get_session)],
    image_id: int
):
    image = await get_product_image_service(
        db=db,
        image_id=image_id
    )

    return image


@router.post('/{product_id}/images')
async def create_product_image(
    db: Annotated[AsyncSession, Depends(get_session)],
    product_id: int,
    alt_text: str,
    validator: Annotated[FileValidator, Depends(get_file_validator)],
    s3: Annotated[S3Storage, Depends(get_s3)],
    mimetype: Annotated[str, Depends(get_mimetype_file)],
    file: UploadFile = File(...)
):
    await create_product_image_service(
        db=db,
        validator=validator,
        file=file,
        product_id=product_id,
        alt_text=alt_text,
        s3=s3,
        mimetype=mimetype
    )


@router.put('/{product_id}/images/{image_id}')
async def update_product_image(
    db: Annotated[AsyncSession, Depends(get_session)],
    validator: Annotated[FileValidator, Depends(get_file_validator)],
    image_id: int,
    alt_text: str,
    s3: Annotated[S3Storage, Depends(get_s3)],
    mimetype: Annotated[str, Depends(get_mimetype_file)],
    file: UploadFile = File(...)
):
    await update_product_image_service(
        db=db,
        validator=validator,
        image_id=image_id,
        alt_text=alt_text,
        file=file,
        s3=s3,
        mimetype=mimetype
    )


@router.delete('/{product_id}/images/{image_id}')
async def delete_product_image():
    pass
