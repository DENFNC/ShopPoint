import uvicorn


from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.router import crud_user
from app.router import crud_shipping
from app.router import crud_payment
from app.router import crud_wishlist
from app.router import authenticate
from app.router import register


router = APIRouter(prefix="/api/v1")
app = FastAPI()


@app.get('/')
async def hello():
    return {
        'message': 'hello world'
    }


app.include_router(router)
app.include_router(authenticate.router)
app.include_router(register.router)
app.include_router(crud_user.router)
app.include_router(crud_payment.router)
app.include_router(crud_shipping.router)
app.include_router(crud_wishlist.router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True
    )
