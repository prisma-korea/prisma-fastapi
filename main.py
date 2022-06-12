from src.apis import apis
from typing import Union

from fastapi import FastAPI

app = FastAPI()
# app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix='/apis')


@app.get("/")
def read_root():
    return {"Hello": "World1111"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
