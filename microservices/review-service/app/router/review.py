from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy import select, update

from app.backend import get_session, AsyncSession
from app.models import Review
from app.schemas import CreateReview, UpdateReview, ReviewInDB

router = APIRouter(prefix='/api/v1/reviews', tags=['Reviews'])


@router.get('/')
async def get_all_review(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    result = await db.scalars(
        select(
            Review
        )
    )

    reviews = result.all()

    return reviews


@router.get('/{review_id}', response_model=ReviewInDB)
async def get_review(
    db: Annotated[AsyncSession, Depends(get_session)],
    review_id: int
):
    async with db.begin():
        result = await db.scalar(
            select(Review)
            .where(
                Review.id == review_id
            )
        )

    return result


@router.post('/')
async def create_review(
    db: Annotated[AsyncSession, Depends(get_session)],
    create: CreateReview
):
    async with db.begin():
        create_review = Review(
            product_id=create.product_id,
            user_id=create.user_id,
            rating=create.rating,
            comment=create.comment
        )

        db.add(create_review)

    return {
        "detail": "Review created successfully"
    }


@router.put('/update/{review_id}')
async def update_review(
    db: Annotated[AsyncSession, Depends(get_session)],
    rew_update: UpdateReview,
    review_id: int
):
    async with db.begin():
        await db.execute(
            update(Review)
            .where(
                Review.id == review_id
            )
            .values(
                rating=rew_update.rating,
                comment=rew_update.comment
            )
        )

    return {
        "detail": "Review updated successfully"
    }


@router.put('/delete/{review_id}')
async def delete_review(
    db: Annotated[AsyncSession, Depends(get_session)],
    review_id: int
):
    async with db.begin():
        await db.execute(
            update(Review)
            .where(
                Review.id == review_id
            )
            .values(
                is_active=False
            )
        )

    return {
        "detail": "Review deleted successfully"
    }
