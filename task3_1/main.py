import uvicorn
from fastapi import FastAPI
from app.models.models import User
from app.models.models import Feedback
from app.models.models import UserCreate
from app.models.models import Product
import json


with open("sample_products.json", "r") as f:
    sample_products = list(json.load(f).values())


app = FastAPI()

fake_users: list[UserCreate] = []
fake_feedbacks = {}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    return {"Error": "Product not found!"}

@app.get("/products/search") 
async def product_search(keyword: str, category: str = "", limit: int = 10) -> list[Product]:
    detected_products = []
    for product in sample_products:
        if keyword.lower() in product['name'].lower() and category.lower() in product['category'].lower():
            detected_products.append(product)
    return detected_products[:limit]


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True, workers=3)