# Example - 1: Default parameter

fake_items_db = [
    {'item_name' : 'Foo'}, {'item_name' : 'Bar'}, {'item_name' : 'Baz'}
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
-------------------------------------------------------------------------------------
# Example - 2: Optional parameter

@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None):
    if q:
        return {"item_id" : item_id,
                 "q" : q}
    return {"item_id" : item_id}
-------------------------------------------------------------------------------------
# Example - 3: Query Parameter Type Conversion

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

http://127.0.0.1:8000/items/foo?short=1
or
http://127.0.0.1:8000/items/foo?short=yes
or
http://127.0.0.1:8000/items/foo?short=on
-------------------------------------------------------------------------------------
# Example - 4: Multiple Path and Query Parameters


@app.get("/users/{user_id}/items/{item_id}/")
async def read_users(
    user_id: int, item_id: str, query: str | None = None, short :bool = False
):
    item = {"item_id" : item_id, "owner_id" : user_id}
    if query:
        item.update({"Query_name" : query})
    if not short:
        item.update({"Inbuild" : "Own_text"})
    return item
-------------------------------------------------------------------------------------
# Example - 5: Required query parameters

@app.get("/items/{item_id}/")
async def read_users(item_id: str, needy: str):
    item = {"item_id" : item_id, "needy" : needy}
    return item
