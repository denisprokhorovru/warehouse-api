from fastapi import FastAPI
from main import Warehouse, DEFAULT_RECIPES

app = FastAPI(title="Warehouse API")

warehouse = Warehouse(recipes=DEFAULT_RECIPES)


@app.get("/quantity/{item_name}")
def get_item_quantity(item_name: str):
    qty = warehouse.get_quantity(item_name)
    return {"item": item_name, "quantity": qty}


@app.get("/warehouse")
def get_warehouse():
    items = warehouse.get_all_items()
    return {"items": items, "total": len(items)}


@app.get("/recipes")
def get_recipes():
    return warehouse.recipes


@app.get("/menu")
def get_menu():
    result = list(warehouse.recipes.keys())
    return {"menu": result}


@app.post("/add")
def add_item(item_name: str, quantity: int):
    warehouse.add_item(item_name, quantity)
    return {"message": f"Товар {item_name} добавлен в количестве {quantity}"}


@app.post("/cook")
def cook(dish_name: str):
    result = warehouse.cook(dish_name)
    return result