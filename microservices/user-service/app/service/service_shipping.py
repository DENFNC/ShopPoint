from sqlalchemy import select, update
from fastapi import HTTPException, status


from app.backend import AsyncSession
from app.schemas import ShippingAddressCreate, ShippingAddressResponse
from app.models import ShippingAddress


async def get_shipping_addresses_service(
    db: AsyncSession
):
    addresses = await db.scalars(
        select(ShippingAddress)
        .where(ShippingAddress.is_active)
    )

    if addresses is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    addresses = addresses.all()

    return addresses


async def get_shipping_address_service(
    db: AsyncSession,
    address_id: int
):
    address = await db.scalars(
        select(ShippingAddress)
        .where(
            ShippingAddress.is_active,
            ShippingAddress.id == address_id
        )
    )

    if address is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    address = address.all()

    return address


async def create_shipping_address_service(
    db: AsyncSession,
    create_address: ShippingAddressCreate
):
    shipping_address = ShippingAddress(
        user_id=create_address.user_id,
        address_line1=create_address.address_line1,
        address_line2=create_address.address_line2,
        city=create_address.city,
        state=create_address.state,
        zip_code=create_address.zip_code,
        country=create_address.country
    )

    db.add(shipping_address)
    await db.commit()


async def update_shipping_address_service(
    db: AsyncSession,
    update_address: ShippingAddressCreate,
    address_id: int
):
    await db.execute(
        update(ShippingAddress)
        .where(
            ShippingAddress.is_active,
            ShippingAddress.id == address_id
        )
        .values(
            user_id=update_address.user_id,
            address_line1=update_address.address_line1,
            address_line2=update_address.address_line2,
            city=update_address.city,
            state=update_address.state,
            zip_code=update_address.zip_code,
            country=update_address.country
        )
    )


async def delete_shipping_address_service(
    db: AsyncSession,
    address_id: int
):
    await db.execute(
        update(ShippingAddress)
        .where(
            ShippingAddress.id == address_id
        )
        .values(
            is_active=False
        )
    )
