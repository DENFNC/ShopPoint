from fastapi import APIRouter, FastAPI
from fastapi_pagination import add_pagination
from app.router import router_product
from app.router import router_static_files
from app.router import router_category


app = FastAPI()
add_pagination(app)

app.include_router(router_product.router)
app.include_router(router_category.router)
app.include_router(router_static_files.router)
