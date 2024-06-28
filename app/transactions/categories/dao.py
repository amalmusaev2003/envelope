from app.dao.base import BaseDAO
from app.transactions.categories.models import Categories

class CategoryDAO(BaseDAO):
    model = Categories