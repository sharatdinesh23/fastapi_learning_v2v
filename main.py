from fastapi import FastAPI
from schemas.product_schema import ProductRequest
app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Welcome to E-Commerce API"
    }

@app.post("/products")
def create_product(product:ProductRequest):
    return {
        "product_name":product.name,
        "product_description":product.description,
        "product_amount":product.price
    }
