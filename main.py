def get_quantity(warehouse, item_name):
    if item_name in warehouse:
        return warehouse[item_name]
    else:
        return 0
    

def remove_item(warehouse, item_name, quantity):
    if item_name in warehouse and warehouse[item_name] >= quantity:
        warehouse[item_name] -= quantity
        return True
    else:
        return False


def cook_omelette(warehouse):
    if get_quantity(warehouse, "яйца") >= 2 and get_quantity(warehouse, "молоко") >= 1:
        remove_item(warehouse, "яйца", 2)
        remove_item(warehouse, "молоко", 1)
        return {"блюдо": "Омлет", "статус": "Готов"}
    elif get_quantity(warehouse, "яйца") < 2:
        return {"статус": "Ошибка", "причина": "Не хватает яиц"}
    elif get_quantity(warehouse, "молоко") < 1:
        return {"статус": "Ошибка", "причина": "Не хватает молока"}


def cook_salad(warehouse):
    if get_quantity(warehouse, "огурцы") >= 2 and get_quantity(warehouse, "помидоры") >= 1 and get_quantity(warehouse, "сметана") >= 1:
        remove_item(warehouse, "огурцы", 2)
        remove_item(warehouse, "помидоры", 1)
        remove_item(warehouse, "сметана", 1)
        return {"блюдо": "Салат", "статус": "Готов"}
    elif get_quantity(warehouse, "огурцы") < 2:
        return {"статус": "Ошибка", "Причина": "Не хватает огурцов"}
    elif get_quantity(warehouse, "помидоры") < 1:
        return {"статус": "Ошибка", "Причина": "Не хватает помидоров"}
    elif get_quantity(warehouse, "сметана") < 1:
        return {"статус": "Ошибка", "Причина": "Не хватает сметаны"}


# Наш склад
inventory = {
    "молоко": 3,
    "яйца": 10,
    "сыр": 1,
    "огурцы": 5,
    "помидоры": 4,
    "сметана": 2
}

# Проверяем работу твоей функции
print(remove_item(inventory, 'молоко', 1))
print(cook_omelette(inventory))
print(cook_salad(inventory))