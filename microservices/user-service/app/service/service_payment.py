from fastapi import HTTPException, status
from sqlalchemy import select, update


from app.backend import AsyncSession
from app.models import User, PaymentMethod
from app.schemas import PaymentMethodCreate


async def get_payment_methods_service(
    db: AsyncSession,
    user_id: int
):
    payment_methods_data = await db.scalars(
        select(PaymentMethod)
        .where(
            PaymentMethod.user_id == user_id,
            PaymentMethod.is_active
        )
    )

    payment_methods_data = payment_methods_data.all()

    return payment_methods_data


async def get_payment_method_service(
    db: AsyncSession,
    payment_id: int
):
    payment_method_data = await db.scalar(
        select(PaymentMethod)
        .where(
            PaymentMethod.id == payment_id,
            PaymentMethod.is_active
        )
    )

    return payment_method_data


async def create_payment_method_service(
    db: AsyncSession,
    create_payment: PaymentMethodCreate,
):
    payment_method = PaymentMethod(
        user_id=create_payment.user_id,
        card_number=create_payment.card_number,
        expiry_date=create_payment.expiry_date,
        cardholder_name=create_payment.cardholder_name,
        billing_address=create_payment.billing_address
    )

    db.add(payment_method)
    await db.commit()


async def update_payment_method_service(
    db: AsyncSession,
    payment_id: int,
    update_payment: PaymentMethodCreate
):
    await db.execute(
        update(PaymentMethod)
        .where(PaymentMethod.id == payment_id)
        .values(
            user_id=update_payment.user_id,
            card_number=update_payment.card_number,
            expiry_date=update_payment.expiry_date,
            cardholder_name=update_payment.cardholder_name,
            billing_address=update_payment.billing_address
        )
    )

    await db.commit()


async def delete_payment_method_service(
    db: AsyncSession,
    payment_id: int
) -> None:
    await db.execute(
        update(PaymentMethod)
        .where(PaymentMethod.id == payment_id)
        .values(
            is_active=False
        )
    )

    await db.commit()
