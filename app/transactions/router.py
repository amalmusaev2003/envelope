from fastapi import APIRouter, Depends
from typing import List

from app.transactions.schemas import STransactionInfo, STransaction, SUpdateTransaction
from app.transactions.dao import TransactionDAO
from app.users.models import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/transactions",
    tags=["Транзакции"]
)

@router.get("")
async def get_all_transactions(user: Users = Depends(get_current_user)) -> List[STransactionInfo]:
    return await TransactionDAO.find_all(user_id=user.id)

@router.get("/month")
async def get_transactions_by_current_month(user: Users = Depends(get_current_user)) -> List[STransactionInfo]:
    return await TransactionDAO.show_last_month(user_id=user.id)

@router.post("")
async def add_transaction(
    transaction: STransaction,
    user: Users = Depends(get_current_user)
):
    return await TransactionDAO.add(user_id=user.id, envelope_id=transaction.envelope_id, category_id=transaction.category_id,
                             amount=transaction.amount, type=transaction.type, date=transaction.date, 
                             description=transaction.description)

@router.delete("/{transaction_id}")
async def remove_transaction(
    transaction_id: int,
    user: Users = Depends(get_current_user)
):
    return await TransactionDAO.delete(id=transaction_id, user_id=user.id)

@router.patch("/{transaction_id}")
async def update_transaction(
    transaction_id: int,
    data: SUpdateTransaction,
    user: Users = Depends(get_current_user)
):
    return await TransactionDAO.update(transaction_id, envelope_id=data.envelope_id, category_id=data.category_id,
                                       amount=data.amount, type=data.type, date=data.date,
                                       description=data.description)