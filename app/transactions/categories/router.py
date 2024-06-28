from fastapi import APIRouter, Depends
from typing import List

from app.users.models import Users
from app.users.dependencies import get_current_user
from app.transactions.categories.dao import CategoryDAO
from app.transactions.categories.schemas import SCategory

router = APIRouter(
    prefix="/transactions/categories",
    tags=["Категории"]
)

@router.get("")
async def get_all_categories(user: Users = Depends(get_current_user)) -> List[SCategory]:
    return await CategoryDAO.find_all(user_id=user.id)

@router.get("/{category_id}")
async def get_category_by_id(
    category_id: int,
    user: Users = Depends(get_current_user)
    ) -> SCategory:
    return await CategoryDAO.find_one_or_none(user_id=user.id, id=category_id)

@router.post("")
async def add_category(
    category: SCategory,
    user: Users = Depends(get_current_user)
):
    return await CategoryDAO.add(name=category.name, user_id=user.id)

@router.delete("/{category_id}")
async def remove_category(
    category_id: int,
    user: Users = Depends(get_current_user)
):
    return await CategoryDAO.delete(id=category_id, user_id=user.id)