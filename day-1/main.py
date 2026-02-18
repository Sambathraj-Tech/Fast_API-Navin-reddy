import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
    return "message : Welcome to my FASTAPI Practice!"

@app.get("/me")
def about_myself(name:str, age:int, city:str, hobby:str):
    return {
        "name" : name,  
        "age" : age,
        "city" : city, 
        "hobby" : hobby
            }

@app.get("/square/{number}")
def maths_square(number: int):
    return {
        "Square" : number * number
    }

@app.get("/multiply")
def multiply(x: int, y: int):
    return {
        "Multiply" : x * y
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


# Step -1:
"""
from fastapi import FastAPI
# Import the FastAPI class — like importing any Python class

app = FastAPI()
# Create your API application — this is your entire API

@app.get("/")
# Decorator! Tells FastAPI:
# "When someone sends a GET request to '/', run the function below"

def read_root():
# A completely normal Python function
# FastAPI calls it when someone visits "/"

    return {"message": "Hello! My API is working!"}
# Return a dictionary → FastAPI automatically converts it to JSON
# and sends it as the HTTP response"""

# Step - 2:
"""
@app.get("/greet/{name}")
def read_name(name: str):
    return f"My name is {name}. Welcome to FastAPI!"

@app.get("/addition_operation")
def read_about(a: int, b: int):
    return {
        "a": a, 
        "b": b, 
        "result": a + b,
        "operation": " addition"
            }
"""
