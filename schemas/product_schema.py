from pydantic import BaseModel, Field, AnyUrl
from typing import List
class CategoryRequest(BaseModel):
    id:int
    name:str

class CategoryResponse(BaseModel):
    name:str

    class Config:
        orm_mode = True

class ProductRequest(BaseModel):
    name:str = Field(min_length=3)
    price:int = Field(gt = 0)
    seller:str
    # description:str= None
    # url:List[AnyUrl] = []
    # category:CategoryRequest



class ProductResponse(BaseModel):
    name:str
    price:int
    # description:str
    # category:CategoryResponse
    # url:List[AnyUrl]
    class Config:
        orm_mode = True
