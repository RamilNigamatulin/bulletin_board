## Описание проекта

Bulletin board  — это Backend-часть для сайта объявлений.

Он разработан с использованием Django и Django REST Framework. 

## Проект включает в себя следующий функционал:

- Пользователи могут регистрироваться, входить в систему и выходить из нее.

- Существуют две роли — пользователь и админ. Админ имеет расширенные права доступа.

- Пользователи могут восстановить забытый пароль, используя свою электронную почту.

- Пользователи могут создавать, читать, обновлять и удалять свои объявления. Админ может управлять всеми объявлениями.

- Пользователи могут оставлять отзывы под объявлениями.

- На сайте реализован поиск объявлений по названию.

- Реализован вывод всех отзывов к объявлению.

## Требования

- Python 3.12
- Docker
- PostgreSQL

## Установка
1. Клонируйте репозиторий: https://github.com/RamilNigamatulin/bulletin_board.git
2. Создайте виртуальное окружение и активируйте его:
    ```
    python -m venv venv
    ```
    ```
    source venv/bin/activate
    ```
3. Переименуйте файл ".env.sample" в ".env" и заполните его.
Для генерации SECRET_KEY введите в консоль команду: 
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
4. Установите зависимости командой: 
    ```
    pip install -r requirements.txt
    ```
5. Запустите проект:
    ```
    python manage.py runserver
    ```
6. Для тестирования проекта возможно использования подготовленных фикстур, для их загрузки введите команду:
    ```
    python manage.py loaddata fixtures/general.json
    ```
    или по отдельности: 
    ```
    python manage.py loaddata fixtures/advertisement.json
    ```
    ```
    python manage.py loaddata fixtures/user.json
    ```
- Пароль для всех пользователей 123qwe.
7. Для использования чистой базы и настройки администратора, внесите соответствующие изменения в файл "csu.py" (логин и пароль администратора) и введите команду: 
    ```
    python manage.py csu
    ```

## Проект подготовлен для упаковки в Docker

Для упаковки и пользования проектом в Docker внесите изменения в настройки файла ".env", а именно "POSTGRES_HOST=db", после чего введите команду:
```
docker-compose up -d --build
```

Откройте приложение в браузере:
- http://localhost:8000/ или http://0.0.0.0:8000/

Для загрузки подготовленных фикстур в проект введите команду:
```
docker-compose exec app python manage.py loaddata fixtures/general.json
```
либо по отдельности каждую фикстуру: 
```
docker-compose exec app python manage.py loaddata fixtures/advertisement.json
```
```
docker-compose exec app python manage.py loaddata fixtures/user.json
```


## Эндпоинты

- **Авторизация и аутентификация**:
  - Регистрация пользователя
    ```
    POST /users/register/
    ``` 
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  - Получение токена
    ```
    POST /users/token/
    ``` 
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  - Обновление токена
    ```
    POST /users/token/refresh/
    ```
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  - Восстановление пароля
    ```
    POST /users/reset_password/
    ```
    ```
    {
      "email": "user@example.ru"
    }
    ```
  - Подтверждение восстановления пароля
    ```
    POST /users/reset_password/confirm/<str:uid>/<str:token>/
    ``` 
    ```
    {
      "new_password_1": "new_example",
      "new_password_2": "new_example"
    }
    ```

- **Объявления**:
  - CRUD для объявлений
    ```
    GET /advertisements/
    ``` 
  - Создание объявления
    ```
    POST /advertisements/create/
    ``` 
    ```
    {
      "title": "example",
      "price": 123
    }
    ```
  - Детальная информация об объявлении
    ```
    GET /advertisements/<int:id>/
    ```
  - Редактирование объявления
    ```
    PUT /advertisements/<int:id>/update/
    ```
    ```
    {
      "title": "example",
      "price": 123
    }
    ```
  - Удаление объявления
    ```
    DELETE /advertisements/<int:id>/delete/
    ```

- **Отзывы**:
  - CRUD для отзывов
    ```
    GET /reviews/
    ``` 
  - Создание отзыва
    ```
    POST /reviews/create/
    ``` 
    ```
    {
      "text": "example",
      "advertisement": "advertisement.id"
    }
    ```
  - Детальная информация об отзыве
    ```
    GET /reviews/<int:id>/
    ```
  - Редактирование отзыва
    ```
    PUT /reviews/<int:id>/update/
    ```
    ```
    {
      "text": "example",
      "advertisement": "advertisement.id"
    }
    ```
  - Удаление объявления
    ```
    DELETE /reviews/<int:id>/delete/
    ```
  - Список отзывов конкретного объявления
    ```
    GET reviews/advertisement/<int:advertisement_id>/
    ```
    
- **Поиск**:
  - Поиск объявлений по названию 
    ```
    GET /advertisements?search=example
    ``` 
    
- **Тестирование**:
    
  ```
  coverage run --source='.' manage.py test
  ```
  ```
  coverage report -m
  ```
