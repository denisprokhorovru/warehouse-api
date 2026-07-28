import pytest
from main import Warehouse

# ====== ФИКСТУРЫ (подготовка объектов для тестов) ======

@pytest.fixture
def empty_warehouse():
    """Пустой склад без товаров и рецептов"""
    return Warehouse()


@pytest.fixture
def stocked_warehouse():
    """Склад с товарами, но без рецептов"""
    return Warehouse({"яйца": 10, "молоко": 5})


@pytest.fixture
def full_warehouse():
    """Склад с товарами и рецептами — как в реальном использовании"""
    return Warehouse(
        {"яйца": 10, "молоко": 5, "огурцы": 4, "помидоры": 3, "сметана": 2},
        recipes={
            "омлет": {"яйца": 2, "молоко": 1},
            "салат": {"огурцы": 2, "помидоры": 1, "сметана": 1}
        }
    )


# ====== ТЕСТЫ ДЛЯ get_quantity ======

def test_get_existing_item(stocked_warehouse):
    """Товар есть — возвращает количество"""
    assert stocked_warehouse.get_quantity("яйца") == 10


def test_get_missing_item(stocked_warehouse):
    """Товара нет — возвращает 0"""
    assert stocked_warehouse.get_quantity("сыр") == 0


def test_get_empty_warehouse(empty_warehouse):
    """Пустой склад — всегда 0"""
    assert empty_warehouse.get_quantity("всё что угодно") == 0


# ====== ТЕСТЫ ДЛЯ remove_item ======

def test_remove_success(stocked_warehouse):
    """Хватает — списывает и возвращает True"""
    result = stocked_warehouse.remove_item("яйца", 3)
    assert result is True
    assert stocked_warehouse.get_quantity("яйца") == 7


def test_remove_not_enough(stocked_warehouse):
    """Не хватает — возвращает False и не меняет остаток"""
    result = stocked_warehouse.remove_item("молоко", 100)
    assert result is False
    assert stocked_warehouse.get_quantity("молоко") == 5  # не изменилось


def test_remove_missing_item(stocked_warehouse):
    """Товара нет — возвращает False"""
    result = stocked_warehouse.remove_item("сыр", 1)
    assert result is False


# ====== ТЕСТЫ ДЛЯ add_item ======

def test_add_new_item(stocked_warehouse):
    """Добавление нового товара"""
    result = stocked_warehouse.add_item("сыр", 3)
    assert result is True
    assert stocked_warehouse.get_quantity("сыр") == 3


def test_add_existing_item(stocked_warehouse):
    """Добавление к существующему товару"""
    result = stocked_warehouse.add_item("яйца", 5)
    assert result is True
    assert stocked_warehouse.get_quantity("яйца") == 15


# ====== ТЕСТЫ ДЛЯ cook ======

def test_cook_success(full_warehouse):
    """Успешное приготовление — ингредиенты списываются"""
    result = full_warehouse.cook("омлет")
    assert result["статус"] == "Готов"
    assert result["блюдо"] == "омлет"
    assert full_warehouse.get_quantity("яйца") == 8
    assert full_warehouse.get_quantity("молоко") == 4


def test_cook_missing_ingredient(full_warehouse):
    """Не хватает ингредиента — ошибка, склад не тронут"""
    full_warehouse.remove_item("молоко", 5)  # убрали всё молоко
    result = full_warehouse.cook("омлет")
    assert result["статус"] == "Ошибка"
    assert "молоко" in result["причина"]
    # Яйца НЕ должны списаться
    assert full_warehouse.get_quantity("яйца") == 10


def test_cook_unknown_dish(full_warehouse):
    """Неизвестное блюдо — ошибка"""
    result = full_warehouse.cook("борщ")
    assert result["статус"] == "Ошибка"
    assert "Рецепт" in result["причина"]


def test_add_to_empty_warehouse(empty_warehouse):
    # 1. Добавляем товар
    empty_warehouse.add_item("хлеб", 5)
    # 2. Проверяем, что хлеб есть и его ровно 5
    assert empty_warehouse.get_quantity("хлеб") == 5