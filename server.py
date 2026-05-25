from fastapi import FastAPI
from main import Warehouse, DEFAULT_RECIPES

app = FastAPI(title="Warehouse API")

warehouse = Warehouse(recipes=DEFAULT_RECIPES)
warehouse.load_from_file("warehouse_data.json")

@app.get("/quantity/{item_name}")
def get_item_quantity(item_name: str):
    qty = warehouse.get_quantity(item_name)
    return {"item": item_name, "quantity": qty}

@app.get("/warehouse")
def get_warehouse():
    return {"items": warehouse.items, "total": len(warehouse.items)}

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
    warehouse.save_to_file("warehouse_data.json")
    return {"message": f"Товар {item_name} добавлен в количестве {quantity}", "item": item_name, "quantity": quantity}

@app.post("/cook")
def cook(dish_name: str):
    result = warehouse.cook(dish_name)
    warehouse.save_to_file("warehouse_data.json")
    return result