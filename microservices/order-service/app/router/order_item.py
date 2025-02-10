from fastapi import APIRouter, Depends


router = APIRouter(prefix='/api/v1/orders', tags=["OrderItems"])


@router.get('/{order_id}/items')
async def get_order_items():
    pass


@router.post('/{order_id}/items')
async def get_order_items():
    pass


@router.patch('/{order_id}/items/{order_item_id}')
async def get_order_items():
    pass


@router.delete('/{order_id}/items/{order_item_id}')
async def get_order_items():
    pass
