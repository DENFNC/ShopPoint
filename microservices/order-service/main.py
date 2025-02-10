from fastapi import FastAPI


from app.router import order, order_item


app = FastAPI()


app.include_router(order.router)
app.include_router(order_item.router)
