from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status


from app.models import Order, OrderItem
from app.schemas import OrderCreate, OrderItemCreate


async def get_orders_service(
    db: AsyncSession
):
    result = await db.scalars(
        select(Order)
        .where(
            Order.is_active
        )
    )

    content = result.all()

    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return content


async def get_order_service(
    db: AsyncSession,
    order_id: int
):
    result = await db.scalars(
        select(Order)
        .where(
            Order.is_active,
            Order.id == order_id
        )
    )

    return result.all()


async def create_order_service(
    db: AsyncSession,
    order_create: OrderCreate,
):
    order = Order(
        user_id=order_create.user_id,
        status=order_create.status,
        total_amount=order_create.total_amount,
        shipping_address_id=order_create.shipping_address_id,
        payment_method_id=order_create.payment_method_id,
    )

    db.add(order)
    await db.flush()

    for item in order_create.items:
        order_item = OrderItem(
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price,
            order_id=order.id
        )
        db.add(order_item)

    await db.commit()
