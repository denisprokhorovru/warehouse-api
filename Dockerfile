# 1. Базовый образ — Python 3.14
FROM python:3.14-slim

# 2. Рабочая папка внутри контейнера
WORKDIR /app

# 3. Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем остальной код
COPY . .

# 5. Команда для запуска
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]