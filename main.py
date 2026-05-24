class Warehouse:
    def __init__(self, initial_items=None, recipes=None):
        if initial_items is None:
            self.items = {}
        else:
            self.items = initial_items
        
        if recipes is None:
            self.recipes = {}
        else:
            self.recipes = recipes
    
    def get_quantity(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            return 0
    
    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            return True
        else:
            return False
    
    def cook(self, dish_name):
        if dish_name not in self.recipes:
            return {"статус": "Ошибка", "причина": f"Рецепт '{dish_name}' не найден"}
    
        recipe = self.recipes[dish_name]

        for ingredient, amount in recipe.items():
            if self.get_quantity(ingredient) < amount:
                return {"статус": "Ошибка", "причина": f"Не хватает {ingredient}"}
    
        for ingredient, amount in recipe.items():
            self.remove_item(ingredient, amount)

        return {"блюдо": dish_name, "статус": "Готов"}
    
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        return True



# Глобальная книга рецептов (можно переиспользовать)
DEFAULT_RECIPES = {
    "омлет": {"яйца": 2, "молоко": 1},
    "салат": {"огурцы": 2, "помидоры": 1, "сметана": 1}
}

# Создаём склад с книгой рецептов
warehouse = Warehouse(
    {"яйца": 10, "молоко": 3, "огурцы": 5, "помидоры": 4, "сметана": 2},
    recipes=DEFAULT_RECIPES
)

print(warehouse.cook("омлет"))
print(warehouse.get_quantity("яйца"))
print(warehouse.get_quantity("молоко"))
print(warehouse.cook("борщ"))
print(warehouse.add_item("яйца", 5))
print(warehouse.get_quantity("яйца"))