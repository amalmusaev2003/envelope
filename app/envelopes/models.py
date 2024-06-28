from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func

from app.database import Base

class Envelopes(Base):
    __tablename__ = "envelopes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(ForeignKey("users.id"))
    balance = Column(Numeric(precision=10, scale=2), default=0.0)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    
    def __str__(self):
        return f"Конверт {self.name}"