from typing import Annotated
from fastapi import APIRouter, Depends


from app.backend import AsyncSession, get_session
from app.service import get_wishlists_service, get_wishlist_service, create_wishlist_service, update_wishlist_service, delete_wishlist_service
from app.schemas import WishlistItemCreate


router = APIRouter(prefix='/api/v1/users', tags=["Wishlist"])


@router.get('/{user_id}/wishlist-items')
async def get_wishlist_items(
    db: Annotated[AsyncSession, Depends(get_session)]
):
    result = await get_wishlists_service(
        db=db
    )

    return result


@router.get('/wishlist-items/{wishlist_item_id}')
async def get_wishlist_item(
    db: Annotated[AsyncSession, Depends(get_session)],
    wishlist_id: int
):
    result = await get_wishlist_service(
        db=db,
        wishlist_id=wishlist_id
    )

    return result


@router.post('/{user_id}/wishlist-items')
async def create_wishlist_item(
    db: Annotated[AsyncSession, Depends(get_session)],
    create_wishlist: WishlistItemCreate,
):
    await create_wishlist_service(
        db=db,
        create_wishlist=create_wishlist
    )

    return


@router.put('/{user_id}/wishlist-items')
async def update_wishlist_item(
    db: Annotated[AsyncSession, Depends(get_session)],
    update_wishlist: WishlistItemCreate,
    wishlist_id: int
):
    await update_wishlist_service(
        db=db,
        update_wishlist=update_wishlist,
        wishlist_id=wishlist_id
    )

    return


@router.delete('/wishlist-items/{wishlist_item_id}')
async def delete_wishlist_item(
    db: Annotated[AsyncSession, Depends(get_session)],
    wishlist_id: int
):
    await delete_wishlist_service(
        db=db,
        wishlist_id=wishlist_id
    )

    return
