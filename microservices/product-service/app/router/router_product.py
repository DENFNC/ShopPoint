from typing import Annotated
from fastapi_pagination.cursor import CursorPage, CursorParams
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi import APIRouter, Depends


from app.backend import AsyncSession, get_session
from app.schemas import ProductResponse, ProductCreate
from app.service import get_product_service, create_product_service, update_product_service, delete_product_service, get_products_service


router = APIRouter(prefix='/api/v1/products', tags=['Product'])


@router.get('/', response_model=CursorPage[ProductResponse])
async def get_products(
    db: Annotated[AsyncSession, Depends(get_session)],
    params: Annotated[CursorParams, Depends()]
):
    result = await get_products_service(
        db=db
    )

    return await paginate(db, result, params)


@router.get('/{product_id}')
async def get_product(
    db: Annotated[AsyncSession, Depends(get_session)],
    product_id: int
):
    result = await get_product_service(
        db=db,
        product_id=product_id
    )

    return result


@router.post('/')
async def create_product(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_product: ProductCreate,
):
    await create_product_service(
        db=db,
        create_product=create_product
    )


@router.put('/')
async def update_product(
    db: Annotated[AsyncSession, Depends(get_session)],
    update_product: ProductCreate,
    product_id: int
):
    await update_product_service(
        db=db,
        update_product=update_product,
        product_id=product_id
    )


@router.delete('/')
async def delete_product(
    db: Annotated[AsyncSession, Depends(get_session)],
    product_id: int
):
    await delete_product_service(
        db=db,
        product_id=product_id
    )
