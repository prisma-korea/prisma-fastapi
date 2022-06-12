from fastapi import APIRouter

from src.apis.users import router 

apis = APIRouter()
apis.include_router(router)

__all__ = ["apis"]
