import json


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
    
    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.items = json.load(f)
        except FileNotFoundError:
            self.items = {}



# Глобальная книга рецептов (можно переиспользовать)
DEFAULT_RECIPES = {
    "омлет": {"яйца": 2, "молоко": 1},
    "салат": {"огурцы": 2, "помидоры": 1, "сметана": 1}
}

# Создаём склад и пополняем
warehouse = Warehouse(recipes=DEFAULT_RECIPES)
warehouse.add_item("яйца", 10)
warehouse.add_item("молоко", 5)

# Сохраняем в файл
warehouse.save_to_file("warehouse_data.json")

# Создаём НОВЫЙ склад и загружаем данные из файла
new_warehouse = Warehouse(recipes=DEFAULT_RECIPES)
new_warehouse.load_from_file("warehouse_data.json")

# Проверяем, что данные загрузились
print(new_warehouse.get_quantity("яйца"))  # → 10
print(new_warehouse.get_quantity("молоко"))  # → 5