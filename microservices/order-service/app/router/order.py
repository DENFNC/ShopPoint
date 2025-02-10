from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.backend import get_session
from app.service import get_order_service, get_orders_service, create_order_service
from app.schemas import OrderCreate


router = APIRouter(prefix='/api/v1/orders', tags=['Order'])


@router.get('/')
async def get_orders(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    result = await get_orders_service(
        db=db
    )

    return result


@router.get('/{order_id}')
async def get_order(
    db: Annotated[AsyncSession, Depends(get_session)],
    order_id: int
):
    result = await get_order_service(
        db=db,
        order_id=order_id
    )

    return result


@router.post('/')
async def create_order(
    db: Annotated[AsyncSession, Depends(get_session)],
    order_create: OrderCreate
):
    await create_order_service(
        db=db,
        order_create=order_create
    )


@router.put('/')
async def update_order():
    pass


@router.patch('/{order_id}/status')
async def update_status():
    pass


@router.delete('/{order_id}')
async def delete_order():
    pass
