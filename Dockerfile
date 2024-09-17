# Используем официальный образ Python
FROM python:3.9-slim

# Указываем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Выполняем миграции и собираем статику
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Команда для запуска приложения
CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT
