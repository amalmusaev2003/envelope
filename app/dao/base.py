from sqlalchemy import select, insert, delete, update
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker

class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()
    
    @classmethod
    async def add(cls, **data):
        try:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            async with async_session_maker() as session:
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()
        except (SQLAlchemyError, Exception) as e:
            print(e)
            return None
        
    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
            return {"detail": "Deleted successfully!"}
        
    @classmethod
    async def update(cls, model_id, **data):
        # Фильтруем словарь, удаляя все ключи со значением None
        filtered_data = {k: v for k, v in data.items() if v is not None}

        if not filtered_data:
            return {"detail": "No data to update"}
        
        async with async_session_maker() as session:
            try:
                query = update(cls.model).where(cls.model.id == model_id).values(**filtered_data)
                result = await session.execute(query)
                await session.commit()

                if result.rowcount == 0:
                    return {"detail": "No matching record found to update"}
            
                return {"detail": "Updated successfully!"}
            except SQLAlchemyError as e:
                print(e)
                return None
