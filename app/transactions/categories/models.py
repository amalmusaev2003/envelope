from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base

class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("users.id"))
    name = Column(String, nullable=False)
    
    def __str__(self):
        return f"Категория {self.name}"