from fastapi import FastAPI
from services.discount import calculate_discount

app = FastAPI()

@app.post("/checkout")
def checkout(cart_total: float, discount: float):
    return {"discount_percentage": calculate_discount(cart_total, discount)}
