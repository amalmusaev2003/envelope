from fastapi import APIRouter, HTTPException, status, Response
from typing import List

from app.users.schemas import SUserAuth
from app.users.dao import UserDAO
from app.users.auth import get_password_hash, authenticate_user, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)

@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(username=user_data.username, email=user_data.email, password_hash=hashed_password)

@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("budget_access_token", access_token, httponly=True)
    return {"access_token": access_token}
