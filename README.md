# Домашнее задание от Urban University

Проект в рамках обучения в Urban University.  
Используемая версия Python 3.12

## Установка

Следуйте этим инструкциям для установки проекта на локальную машину для разработки и тестирования.
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/ZehrBit/DZ_djangoProject.git
    cd DZ_djangoProject
    ```
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Создайте базу данных и выполните миграции:
    ```bash
    python manage.py migrate
    ```
5. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
6. Запустите сервер разработки:
    ```bash
    python manage.py runserver
   ```
7. Заполните базу данных, перейдя по ссылке в вашем браузере:
   ```bash
   http://127.0.0.1:8000/admin/
   ```
8. Перейдите по адресу в вашем браузере, чтобы увидеть работающий проект.
   ```bash
   http://127.0.0.1:8000/
   ```

## Контакты
Email: zehrbit@gmail.com  
Telegram: https://t.me/zehrbit
