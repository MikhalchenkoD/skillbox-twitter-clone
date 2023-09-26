# Используем официальный образ Python в качестве базового образа
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY fastapi/requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем весь код приложения FastAPI в контейнер
COPY fastapi /app

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

VOLUME /app/uploadfile

# Команда для запуска приложения
CMD ["uvicorn", "routes:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
