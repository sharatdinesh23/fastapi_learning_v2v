from fastapi import FastAPI
from schemas.product_schema import ProductRequest,ProductResponse
from schemas.user_schema import SellerUserRequest,SellerUserResponse

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Welcome to E-Commerce API"
    }

@app.post("/products",response_model= ProductResponse)
def create_product(product:ProductRequest):
    return product

@app.post("/seller",response_model = SellerUserResponse)
def create_seller(seller:SellerUserRequest):
    return seller


