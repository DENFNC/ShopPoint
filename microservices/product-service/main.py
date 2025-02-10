from typing import Any, Dict
from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from app.router import product, static_files


from app.config import settings


router = APIRouter(prefix="/api/v1")


@router.get('/')
async def hello_product() -> Dict[str, Any]:
    return {
        'message': 'Привет!'
    }

app = FastAPI()
add_pagination(app)

app.mount('/static', StaticFiles(directory=settings.BASE_FILE_PATH), name='static')
app.include_router(router)
app.include_router(product.router)
# # app.include_router(supplier.router)
app.include_router(static_files.router)
