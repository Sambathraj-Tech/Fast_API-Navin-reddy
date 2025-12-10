from fastapi import FastAPI

app = FastAPI()

# FastAPI allows you to declare additional information and validation for your parameters.
@app.get("/items")
async def read_items(q: str | None = None):
    result = {"items": [{"item_id" : "foo"}, {"item_id" : "Bar"}]}
    if q:
        result.update({"item_id" : "Baz"})
    return result

# Additional validation
# Even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

----------------------------------------------------------------------------------------------
# Import Query and Annotated

from typing import Annotated
from fastapi import Query

@app.get("/items1")
async def read_items(q: Annotated[str | None , Query(max_length = 50)] = None):
    result = {"items": [{"item_id" : "foo"}, {"item_id" : "Bar"}]}
    if q:
        result.update({"item_id" : "Baz"})
    return result
----------------------------------------------------------------------------------------------
# Default values
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
