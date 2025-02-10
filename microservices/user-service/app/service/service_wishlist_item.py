from sqlalchemy import select, update


from app.backend import AsyncSession
from app.models import WishlistItem
from app.schemas import WishlistItemCreate


async def get_wishlists_service(
    db: AsyncSession
):
    wishlists = await db.scalars(
        select(WishlistItem)
        .where(
            WishlistItem.is_active
        )
    )

    wishlists = wishlists.all()

    return wishlists


async def get_wishlist_service(
    db: AsyncSession,
    wishlist_id: int
):
    wishlist = await db.scalars(
        select(WishlistItem)
        .where(
            WishlistItem.is_active,
            WishlistItem.id == wishlist_id
        )
    )

    wishlist = wishlist.all()

    return wishlist


async def create_wishlist_service(
    db: AsyncSession,
    create_wishlist: WishlistItemCreate
):
    wishlist = WishlistItem(
        user_id=create_wishlist.user_id,
        product_id=create_wishlist.product_id
    )

    db.add(wishlist)
    await db.commit()


async def update_wishlist_service(
    db: AsyncSession,
    update_wishlist: WishlistItemCreate,
    wishlist_id: int
):
    await db.execute(
        update(WishlistItem)
        .where(
            WishlistItem.id == wishlist_id
        )
        .values(
            user_id=update_wishlist.user_id,
            product_id=update_wishlist.product_id
        )
    )

    return


async def delete_wishlist_service(
    db: AsyncSession,
    wishlist_id: int
):
    await db.execute(
        update(WishlistItem)
        .where(
            WishlistItem.id == wishlist_id
        )
        .values(
            is_active=False
        )
    )

    return
