from typing import Annotated
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.backend import get_session
from app.schemas import CreateCategory
from app.schemas import UpdateCategory
from app.service import get_categories_service
from app.service import get_category_service
from app.service import create_category_service
from app.service import update_category_service
from app.service import delete_category_service


router = APIRouter(prefix='/api/v1', tags=['Category'])


@router.get('/categories')
async def get_categories(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    result = await get_categories_service(
        db=db
    )

    return result


@router.get('/categories/{category_id}')
async def get_category(
    db: Annotated[AsyncSession, Depends(get_session)],
    category_id: int
):
    result = await get_category_service(
        db=db,
        category_id=category_id
    )

    return result


@router.post('/categories')
async def create_category(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_category: CreateCategory
):
    await create_category_service(
        db=db,
        create_category=create_category
    )

    return


@router.put('/categories/{category_id}')
async def update_category(
    db: Annotated[AsyncSession, Depends(get_session)],
    category_id: int,
    update_category: UpdateCategory
):
    await update_category_service(
        db=db,
        category_id=category_id,
        update_category=update_category
    )

    return


@router.delete('/categories/{category_id}')
async def delete_category(
    db: Annotated[AsyncSession, Depends(get_session)],
    category_id: int
):
    await delete_category_service(
        db=db,
        category_id=category_id
    )
