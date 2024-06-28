from pydantic import BaseModel, EmailStr
from datetime import datetime

class SUsersInfo(BaseModel):
    username: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True

class SUserAuth(BaseModel):
    username: str
    email: EmailStr
    password: str