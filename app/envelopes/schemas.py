from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional

class SEnvelope(BaseModel):
    name: str
    description: str
    balance: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

class SNewEnvelope(BaseModel):
    name: str
    description: str
    balance: Decimal

class SUpdateEnvelope(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    balance: Optional[Decimal] = None