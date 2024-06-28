from fastapi import Depends, Request, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime

from app.config import settings
from app.users.dao import UserDAO
from app.exceptions import IncorrectTokenFormatException, TokenExpiredException, UserIsNotPresentException

def get_token(request: Request):
    token = request.cookies.get("budget_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is not found")
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UserDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user