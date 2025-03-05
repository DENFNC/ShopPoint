from fastapi import FastAPI
from app.router import router_user
from app.router import router_role


app = FastAPI(debug=True)


app.include_router(router_user.router)
app.include_router(router_role.router)
