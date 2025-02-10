from tkinter.messagebox import RETRY
from typing import Annotated, List
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select


from app.backend import AsyncSession, get_session
from app.models import Category
from app.schemas import CategoryResponse, CategoryCreate
from app.service import get_active_categories, get_active_category, get_create_category


router = APIRouter(prefix="/api/v1/categories", tags=["Categories"])


@router.get('/')
async def get_all_categories(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    categories = await get_active_categories(db)

    return {
        'Categories': categories
    }


@router.get('/{category_id}')
async def get_category(
    db: Annotated[AsyncSession, Depends(get_session)],
    category_id: int
):
    category = await get_active_category(
        db=db,
        category_id=category_id
    )

    return category


@router.post('/')
async def create_category(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_category: CategoryCreate
):
    await get_create_category(
        db=db,
        create_category=create_category
    )

    return {
        'Message': 'Category created successfully'
    }
