from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime


class STransaction(BaseModel):
    envelope_id: Optional[int] = None
    category_id: int
    amount: float
    type: str
    date: datetime
    description: str
    
    class Config():
        from_attributes = True

class STransactionInfo(BaseModel):
    envelope_name: Optional[str] = None
    category_name: str
    amount: float
    type: str
    date: datetime
    description: str

    class Config():
        from_attributes = True

class SUpdateTransaction(BaseModel):
    envelope_id: Optional[int] = None
    category_id: Optional[int] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    date: Optional[datetime] = None
    description: Optional[str] = None