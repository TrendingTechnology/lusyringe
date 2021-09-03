from rests import routers
from fastapi import FastAPI


app = FastAPI()

for router in routers:
    app.include_router(router)
