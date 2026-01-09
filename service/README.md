# ServiceAPI

Данный API предназначен для управления биржей услуг

# Использованные технологии:
1. Django
2. Django REST Framework
3. drf-yasg
4. JWT (SimpleJWT)
5. SQLite
6. Docker

# Установка и запуск
1. Скачайте zip-файл и распакуйте в удобной для вас папке
2. Запустите Docker-compose: docker-compose up --build
3. Примените миграции: docker-compose exec service-web-1 python manage.py migrate
4. Создайте суперпользователя: docker-compose exec service-web-1 python manage.py createsuperuser
5. Далее вам будет представлена страница с путями, чтобы начать работу с данными в Swagger, перейдите по пути: /swagger
6. Также не забудьте получить токен через путь /token отправив запрос: POST /api/token/ { "username": "admin", "password": "password" }
7. После для авторизации вставьте токен В Swagger: Bearer <access_token>
