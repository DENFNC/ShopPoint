from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def hello():
    return {'message': 'Welcome to the ShopPoint API'}
