from fastapi import FastAPI
from schemas.product_schema import ProductRequest,ProductResponse
from schemas.seller_schema import SellerUserRequest,SellerUserResponse
from schemas.orders_schema import OrderRequest, OrderResponse
from routers.orders_router import order_router

app = FastAPI(
    title = "E-Commerce Backend API",
    description = "Welcome to V2V internship",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {
        "message":"Welcome to E-Commerce API"
    }
app.include_router(order_router)

@app.post("/products",response_model= ProductResponse,tags = ["Product"])
def create_product(product:ProductRequest):
    return product

@app.post("/seller",response_model = SellerUserResponse,tags = ["Seller"])
def create_seller(seller:SellerUserRequest):
    return seller

