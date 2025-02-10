from fastapi import FastAPI

from app.router import review

app = FastAPI()


app.include_router(review.router)
