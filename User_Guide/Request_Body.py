EX - 1: Create BaseModel and Passing the Parameter

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items")
async def create_items(item: Item):
    return item
============================================================
