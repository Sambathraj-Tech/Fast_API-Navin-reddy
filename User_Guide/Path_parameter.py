from fastapi import FastAPI

app = FastAPI()

# Path parameters with types
@app.get("/items/{item_id}")
async def read_items_id(item_id: int):
    return f"item_id : {item_id}"


@app.get("/items/{item_str}")
async def read_items_string(item_name: str):
    return f"item nmae : {item_name}"

# Order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user_id(user_id: str):
    return {"User_id" : user_id}

@app.get("/users")
async def read_users():
    return ["Sambath", "Raj"]

@app.get("/users")
async def read_users2():
    return ["Ragavan", "Ram"]

# Predefined Values

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet  = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return f"model_name : {model_name}, message : Deep Learning FTW"
    elif model_name is ModelName.resnet:
        return f"model_name : {model_name}, message : LeCNN all the images"
    
    return f"model_name : {model_name}, message : Have some residuals"
