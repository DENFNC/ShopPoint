from fastapi import FastAPI

from app.router import categories

app = FastAPI()

app.include_router(categories.router)
