import uvicorn


from fastapi import FastAPI
from fastapi import APIRouter


from app.router import router_user
from app.router import router_shipping
from app.router import router_payment
from app.router import router_wishlist


router = APIRouter(prefix="/api/v1")
app = FastAPI()


app.include_router(router)
app.include_router(router_user.router)
app.include_router(router_payment.router)
app.include_router(router_shipping.router)
app.include_router(router_wishlist.router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True
    )
