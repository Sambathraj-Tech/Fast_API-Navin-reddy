# Example - 1

fake_items_db = [
    {'item_name' : 'Foo'}, {'item_name' : 'Bar'}, {'item_name' : 'Baz'}
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
-------------------------------------------------------------------------------------
# Example - 2

@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None):
    if q:
        return {"item_id" : item_id,
                 "q" : q}
    return {"item_id" : item_id}
-------------------------------------------------------------------------------------
# Example - 3

