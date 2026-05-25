# Warehouse API

API для управления складом и приготовления блюд. Учебный проект для стажировки Python-разработчика.

## Стек
- Python 3.x
- FastAPI
- Uvicorn

## Запуск

1. Клонируйте репозиторий:  
   `git clone https://github.com/denisprokhorovru/warehouse-api.git`  
   `cd warehouse-api`

2. Создайте и активируйте виртуальное окружение:  
   `python -m venv .venv`  
   `source .venv/Scripts/activate` *(Windows)*  
   `source .venv/bin/activate` *(Mac/Linux)*

3. Установите зависимости:  
   `pip install -r requirements.txt`

4. Запустите сервер:  
   `uvicorn server:app --reload`

5. Откройте документацию API:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🔌 API Endpoints

### Склад

| Метод | URL | Описание | Пример |
|-------|-----|----------|--------|
| `GET` | `/warehouse` | Получить все остатки на складе | `/warehouse` |
| `GET` | `/quantity/{item}` | Остаток конкретного товара | `/quantity/яйца` |
| `POST` | `/add` | Добавить товар | `/add?item_name=яйца&quantity=10` |

### Рецепты

| Метод | URL | Описание | Пример |
|-------|-----|----------|--------|
| `GET` | `/recipes` | Все рецепты с ингредиентами | `/recipes` |
| `GET` | `/menu` | Список доступных блюд | `/menu` |
| `POST` | `/cook` | Приготовить блюдо | `/cook?dish_name=омлет` |

## Консольная версия

Также доступен консольный интерфейс:  
`python main.py`