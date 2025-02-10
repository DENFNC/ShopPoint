from fastapi import FastAPI

from app.router import supplier


app = FastAPI()


app.include_router(supplier.router)
