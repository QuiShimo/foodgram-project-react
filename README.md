# Foodgram
[![Django-app workflow](https://github.com/QuiShimo/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/QuiShimo/foodgram-project-react/actions/workflows/main.yml)

## Опиание проекта.
Сайт Foodgram, «Продуктовый помощник». Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Используемые технологии
- Python 3.11
- Django 4.2.1
- Django REST framework 3.14
- Postgres
- Nginx
- Docker

## Возможности

- Просматривать рецепты
- Добавлять рецепты в избранное
- Добавлять рецепты в список покупок
- Создавать, удалять и редактировать собственные рецепты
- Скачивать список покупок

## Инструкция по развертыванию
### Локально
- Клонируйте репозиторий:
```
git clone git@github.com:QuiShimo/foodgram-project-react.git
```
- Установите и активируйте виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Примените миграции:

```
python manage.py migrate
```
- В папке с файлом manage.py выполните команду для запуска локально:

``` 
python manage.py runserver
```
- Локально Документация доступна по адресу:

http://127.0.0.1/api/docs/

### С помощью Docker:
Из папки infra/ разверните контейнеры при помощи docker-compose:

```
docker-compose up -d --build 
```
Выполните миграции:

```
docker-compose exec backend python manage.py migrate
```
Создайте суперпользователя:

```
docker-compose exec backend python manage.py createsuperuser
```
Соберите статику:

```
docker-compose exec backend python manage.py collectstatic --no-input
```
Наполните базу данных ингредиентами и тегами. Выполняйте команду из дериктории где находится файл manage.py:
```
docker-compose exec backend python manage.py load_data
```

 Остановка проекта:
```
docker-compose down
```


## Примеры запросов:
- POST | Создание рецепта: /api/recipes/

Request:
```
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```
Response:
```
{
  "id": 0,
  "tags": [
    {
      "id": 0,
      "name": "Завтрак",
      "color": "#E26C2D",
      "slug": "breakfast"
    }
  ],
  "author": {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "is_subscribed": false
  },
  "ingredients": [
    {
      "id": 0,
      "name": "Картофель отварной",
      "measurement_unit": "г",
      "amount": 1
    }
  ],
  "is_favorited": true,
  "is_in_shopping_cart": true,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "text": "string",
  "cooking_time": 1
}
```


POST | Подписаться на пользователя: /api/users/{id}/subscribe/

Response:
```
{
  "email": "user@example.com",
  "id": 0,
  "username": "string",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "is_subscribed": true,
  "recipes": [
    {
      "id": 0,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "cooking_time": 1
    }
  ],
  "recipes_count": 0
}
```
