from src.apis import apis
from typing import Union
from prisma import Prisma

from fastapi import FastAPI

prisma = Prisma()

app = FastAPI()
# app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix='/apis')

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

@app.get("/")
async def read_root():
    users = await prisma.user.find_many();
    return {"users": users}
