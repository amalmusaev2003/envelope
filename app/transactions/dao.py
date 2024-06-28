import datetime
from app.dao.base import BaseDAO
from sqlalchemy import select, and_, func, extract
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.transactions.models import Transactions
from app.transactions.categories.models import Categories
from app.envelopes.models import Envelopes

class TransactionDAO(BaseDAO):
    model = Transactions

    @classmethod
    async def find_all(cls, user_id: int):
        '''
        select transactions.id, transactions.user_id, transactions.envelope_id,
                transactions.category_id, transactions.amount,
                transactions.type, transactions.date, transactions.created_at,
                transactions.updated_at, envelopes.name as 'envelope_name',
                categories.name as 'category_name'
        from transactions
        inner join envelopes on transactions.envelope_id = envelopes.id
        inner join envelopes on transactions.category_id = categories.id
        '''
        async with async_session_maker() as session:
            query = (
                select(
                    Transactions.__table__.columns,
                    Envelopes.name.label("envelope_name"),
                    Categories.name.label("category_name")
                )
                .join(Envelopes, Transactions.envelope_id == Envelopes.id)
                .join(Categories, Transactions.category_id == Categories.id)
                .where(Transactions.user_id == user_id)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def show_last_month(cls, user_id: int):
        now = datetime.datetime.now()
        current_month = now.month
        current_year = now.year
        async with async_session_maker() as session:
            query = (
                select(
                    Transactions.__table__.columns,
                    Envelopes.name.label("envelope_name"),
                    Categories.name.label("category_name")
                )
                .join(Envelopes, Transactions.envelope_id == Envelopes.id)
                .join(Categories, Transactions.category_id == Categories.id)
                .where(and_(
                    Transactions.user_id == user_id,
                    extract('month', Transactions.date) == current_month,
                    extract('year', Transactions.date) == current_year
                    )
                )
            )
            result = await session.execute(query)
            return result.mappings().all()
            