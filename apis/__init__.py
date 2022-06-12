from fastapi import APIRouter

from apis.users import router 

apis = APIRouter()
apis.include_router(router)

__all__ = ["apis"]
