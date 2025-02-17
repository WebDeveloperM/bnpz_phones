# Python bazasini tanlash
FROM python:3.9-slim

# Ishlash papkasini yaratish
WORKDIR /app

# PostgreSQL uchun kerakli kutubxonalarni o‘rnatish
RUN apt-get update && apt-get install -y gcc libpq-dev

# Talablar faylini qo‘shish va pip o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Django loyihasini qo‘shish
COPY . .

# Portni ochish
EXPOSE 8000

# Django serverini ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
