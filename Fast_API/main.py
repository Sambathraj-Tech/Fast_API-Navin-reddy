from fastapi import Depends, FastAPI # class name
from models import Product # class name
from database import session, engine
import database_models
from sqlalchemy.orm import Session


app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to FastApi"


products = [
    Product(id = 1,name = "Iphone",description = "Apple chip",price = 500000.0,quantity = 5),
    Product(id = 2,name = "Macbook",description = "Apple Laptop",price = 1000000.0,quantity = 5),
    Product(id = 3,name = "Macbook-Air",description = "Apple Laptop",price = 99000,quantity = 1),
    Product(id = 4,name = "Macbook-Pro",description = "Apple laptop",price = 160000.0,quantity = 1),
]

# Injection
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# addvalues to the sql
def init_db():
    db = session()

    count = db.query(database_models.Product).count

    count = 0
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        #                 package         Class     object. dictionary(key:value_pairs)   (** -> Unpacking) 
        db.commit() # add f
init_db()

# Get all values
@app.get("/products")               # Injected
def get_all_products(db : Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    return db_products

# Get values by ID
@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

# Adding new values
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

# Update product by id  
@app.put("/product") 
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:  # product[0].0, 1, 2, 3
            products[i] = product
            return "Product Added Succesfully"
    return "Product not added"
 
# Delete product by id
@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted Successfully"
    return "Product not found"