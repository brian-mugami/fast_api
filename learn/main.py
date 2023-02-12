from fastapi import FastAPI
from . import models
from .routers import userrouter, itemrouter, authrouter


from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(itemrouter)
app.include_router(userrouter)
app.include_router(authrouter)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}



