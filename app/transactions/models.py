from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, DateTime, ForeignKey, Enum, func

from app.database import Base

class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("users.id"))
    envelope_id = Column(ForeignKey("envelopes.id"))
    category_id = Column(ForeignKey("categories.id"))
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    type = Column(Enum('income', 'expense', name='transaction_types'), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __str__(self):
        return f"Транзакция на сумму f{self.amount}"