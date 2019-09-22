# SimpleWeb

## Требования
* Python 3.7
* SQLite
* Django Framework > 2.2

## Подготовка к запуску 
Необходимос скачать интерпретатор python 3.7 (https://www.python.org/downloads/).<br>
Создать виртуальное окружение в папке проекта, выполнив команду:<br>

>python -m venv env

Активировать виртуальное окружение:

>\env\Scripts\activate.bat

Установить необходимые модули python:

>pip install -r requirements.txt</code>

Добавить суперпользователя в БД

>python manage.py makemigrations
>
>python manage.py migrate
>
>python manage.py adminuser

Можно добавить тестовые данные

> python manage.py sampledata

## Запуск
> python manage.py runserver 0.0.0.0


