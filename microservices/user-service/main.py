from typing import Annotated
from fastapi import APIRouter, Depends, FastAPI, Form, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.backend import AsyncSession, get_session


from app.router import crud_user, authenticate, crud_payment, crud_shipping, crud_wishlist
from app.core import get_current_username


class Message(BaseModel):
    body: str


router = APIRouter(prefix="/api/v1")


origins = [
    'http://localhost:5173',
    'http://127.0.0.1:5173'
]


@router.get('/')
async def hello_world():
    return {'message': 'Hello!'}


@router.get('/username')
async def get_username(
    db: Annotated[AsyncSession, Depends(get_session)],
    user_id: int = Query(...)
):
    result = await get_current_username(
        db=db,
        user_id=user_id
    )

    return result


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(authenticate.router)
# app.include_router(register.router)
app.include_router(crud_user.router)
app.include_router(crud_payment.router)
app.include_router(crud_shipping.router)
app.include_router(crud_wishlist.router)
