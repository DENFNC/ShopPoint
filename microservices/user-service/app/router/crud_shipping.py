from typing import Annotated
from fastapi import APIRouter, Depends

from app.backend import AsyncSession, get_session
from app.schemas import ShippingAddressCreate, ShippingAddressResponse
from app.service import (
    get_shipping_addresses_service,
    get_shipping_address_service,
    create_shipping_address_service,
    update_shipping_address_service,
    delete_shipping_address_service
)


router = APIRouter(prefix='/api/v1/users', tags=['Shipping Addresses'])


@router.get('/{user_id}/shipping-addresses')
async def get_shipping_addresses(
    db: Annotated[AsyncSession, Depends(get_session)],
):
    result = await get_shipping_addresses_service(
        db=db
    )

    return result


@router.get('/shipping-addresses/{address_id}')
async def get_shipping_address():
    pass


@router.post('/{user_id}/shipping_addresses')
async def create_shipping_address(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_address: ShippingAddressCreate
):
    await create_shipping_address_service(
        db=db,
        create_address=create_address
    )

    return


@router.put('/shipping-addresses/{address_id}')
async def update_shipping_address():
    pass


@router.delete('/shipping-addresses/{address_id}')
async def delete_shipping_address():
    pass
