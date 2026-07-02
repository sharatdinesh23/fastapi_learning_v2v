from pydantic import BaseModel


class ProductRequest(BaseModel):
    name:str
    price:int
    description:str= None
