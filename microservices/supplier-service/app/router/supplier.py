from typing import Annotated, Dict, List
from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.backend import get_session, AsyncSession
from app.models import Supplier
from app.schemas import SupplierCreate, SupplierInDB


router = APIRouter(prefix='/supplier', tags=['Supplier'])


@router.get('/', response_model=Dict[str, List[SupplierInDB]])
async def get_all_suppliers(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    result = await db.scalars(
        select(Supplier)
    )

    return {
        'suppliers': result.all()
    }


@router.get('/{supplier_id}', response_model=SupplierInDB)
async def get_supplier(
    db: Annotated[AsyncSession, Depends(get_session)],
    supplier_id: int
):
    result = await db.scalars(
        select(Supplier)
        .where(Supplier.id == supplier_id)
    )

    supplier = result.first()

    return supplier


@router.post('/')
async def create_supplier(
    db: Annotated[AsyncSession, Depends(get_session)],
    sup_create: SupplierCreate
):
    async with db.begin():
        supplier = Supplier(
            name=sup_create.name,
            contact_email=sup_create.contact_email,
            phone_number=sup_create.phone_number,
            address=sup_create.address,
        )

        db.add(supplier)

    return {
        "detail": "Supplier created successfully"
    }
