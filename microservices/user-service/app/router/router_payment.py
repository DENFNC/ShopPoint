from typing import Annotated, Dict, List
from fastapi import APIRouter, Depends, status


from app.backend import AsyncSession, get_session
from app.service import create_payment_method_service, get_payment_methods_service, update_payment_method_service, delete_payment_method_service, get_payment_method_service
from app.schemas import PaymentMethodCreate, PaymentMethodResponse


router = APIRouter(prefix='/api/v1/users', tags=['Payment'])


@router.get('/{user_id}/payment-methods', response_model=Dict[str, List[PaymentMethodResponse]])
async def get_payments_method(
    db: Annotated[AsyncSession, Depends(get_session)],
    user_id: int
):
    payment = await get_payment_methods_service(
        db=db,
        user_id=user_id
    )

    return {
        'PaymentMethods': payment
    }


@router.get('/payment-methods/{payment_id}/', status_code=status.HTTP_200_OK, response_model=PaymentMethodResponse)
async def get_payment_method(
    db: Annotated[AsyncSession, Depends(get_session)],
    payment_id: int
):
    payment = await get_payment_method_service(
        db=db,
        payment_id=payment_id
    )

    return payment


@router.post('/payment-methods/{payment_id}', status_code=status.HTTP_201_CREATED)
async def create_payment_method(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_payment: PaymentMethodCreate
) -> None:
    await create_payment_method_service(
        db=db,
        create_payment=create_payment,
    )


@router.put('/payment-methods/{payment_id}', status_code=status.HTTP_200_OK)
async def update_payment_method(
    db: Annotated[AsyncSession, Depends(get_session)],
    update_payment: PaymentMethodCreate,
    payment_id: int
) -> None:
    await update_payment_method_service(
        db=db,
        payment_id=payment_id,
        update_payment=update_payment
    )

    return


@router.delete('/payment-methods/{payment_id}', status_code=status.HTTP_200_OK)
async def delete_payment_method(
    db: Annotated[AsyncSession, Depends(get_session)],
    payment_id: int
) -> None:
    await delete_payment_method_service(
        db=db,
        payment_id=payment_id
    )

    return
