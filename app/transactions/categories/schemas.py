from pydantic import BaseModel

class SCategory(BaseModel):
    name: str

    class Config():
        from_attributes = True 
