from pydantic import BaseModel, EmailStr, Field

class SellerUserRequest(BaseModel):
    name:str = Field(min_length=3)
    email:EmailStr

class SellerUserResponse(BaseModel):
    name:str
    email:EmailStr

    class Config:
        orm_mode = True
