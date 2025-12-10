EX - 1: Create BaseModel and Passing the Parameter

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# Base Model

@app.post("/items")
async def create_items(item: Item):
    return item
    
============================================================
# Use the model
@app.post("/itemss")
async def update_items(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.tax + item.price
        item_dict.update({"price_with_tax" : price_with_tax})
    return item_dict
    
============================================================
# Request body + path parameters
@app.put("/users/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id" : item_id, **item.dict()}

============================================================
# Request body + path + query parameters
@app.put("/user1")
async def update_item(item_id: int, item: Item, query: str | None = None):
    result = {"item_id" : item_id, **item.dict()}
    if query:
        result.update({"Query" : query})
    return result
============================================================
