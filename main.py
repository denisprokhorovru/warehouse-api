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


def main():
    # Создаём склад
    warehouse = Warehouse(recipes=DEFAULT_RECIPES)
    warehouse.load_from_file("warehouse_data.json")
    
    print("Добро пожаловать в систему управления складом!")
    print("Доступные команды: остаток, добавить, приготовить, рецепты, склад, выход")
    
    while True:
        command = input("\nВведите команду: ").strip().lower()
        parts = command.split()
        
        if not parts:
            continue
        
        if parts[0] == "выход":
            print("До свидания!")
            break
        
        elif parts[0] == "остаток":
            if len(parts) < 2:
                print("Укажите товар: остаток <название>")
                continue
            item = parts[1]
            qty = warehouse.get_quantity(item)
            print(f"Товар: {item}, Количество: {qty}")
        
        elif parts[0] == "добавить":
            if len(parts) < 3:
                print("Ошибка! Формат команды: добавить <название> <количество>")
                continue
                
            item_name = parts[1]
            
            try:
                quantity = int(parts[2])
            except ValueError:
                print("Ошибка! Количество должно быть целым числом.")
                continue
        
            warehouse.add_item(item_name, quantity)
            print(f"Успешно добавлено: {item_name} в количестве {quantity}")
 
        elif parts[0] == "приготовить":
            if len(parts) < 2:
                print("Ошибка! Формат команды: приготовить <название рецепта>")
                continue

            result = warehouse.cook(parts[1])
            
            if result["статус"] == "Ошибка":
                print(f"Ошибка! Причина {result['причина']}")
            else:
                print(f"Блюдо {result['блюдо']} успешно приготовлено!")

        
        elif parts[0] == "рецепты":
            if not warehouse.recipes:
                print("Нет доступных рецептов.")
            else:
                for recipe_name in warehouse.recipes.keys():
                    print(f"Доступный рецепт: {recipe_name}")
        
        elif parts[0] == "склад":
            if not warehouse.items:
                print("Склад пуст.")
            else:
                for name, quantity in warehouse.items.items():
                    print(f"Текущий склад: {name} = {quantity}")
        
        else:
            print(f"Неизвестная команда: {parts[0]}")
        
        # Сохраняем после каждого действия
        warehouse.save_to_file("warehouse_data.json")


if __name__ == "__main__":
    main()
