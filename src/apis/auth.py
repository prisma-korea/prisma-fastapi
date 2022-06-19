import datetime
from typing import List, Optional
from fastapi import APIRouter
from prisma.models import User
from pydantic import BaseModel
from src.models.scalar import Gender
from src.prisma import prisma
from src.utils.auth import (
    encryptPassword,
    signJWT,
    validatePassword,
)

router = APIRouter()


class SignIn(BaseModel):
    email: str
    password: str


class SignInOut(BaseModel):
    token: str
    user: User


@router.post("/auth/sign-in", tags=["auth"])
async def sign_in(signIn: SignIn):
    user = await prisma.user.find_first(
        where={
            "email": signIn.email,
        }
    )

    validated = validatePassword(signIn.password, user.password)
    del user.password

    if validated:
        token = signJWT(user.id)
        return SignInOut(token=token, user=user)

    return None


class SignUp(BaseModel):
    email: str
    password: str
    name: Optional[str] = None
    nickname: Optional[str] = None
    birthday: Optional[datetime.date] = None
    gender: Optional[Gender] = None
    phone: Optional[str] = None


@router.post("/auth/sign-up", tags=["auth"])
async def sign_up(user: SignUp):
    password = encryptPassword(user.password)
    created = await prisma.user.create(
        {
            "email": user.email,
            "password": encryptPassword(user.password),
            "name": user.name,
            "nickname": user.nickname,
            "birthDay": user.birthday,
            "gender": user.gender,
            "phone": user.phone,
        }
    )

    return created


@router.get("/auth/", tags=["auth"])
async def auth():
    users = await prisma.user.find_many()

    for user in users:
        del user.password

    return users
