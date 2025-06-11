
Documentation
[a link](https://dev.to/yahiaqous/how-to-build-a-crud-api-using-python-flask-and-sqlalchemy-orm-with-postgresql-2jjj)

1) Setup `Pipenv` on your local machine. It's a dependency-manager for Python projects. 
```shell
pip install pipenv
```
2) Install project dependencies. 
```shell
pipenv install -r src/requirements.txt
```
3) Activate virtual environment
```shell
pipenv shell
```
4) To check active env location
```shell
pip -V
```
5) to deactivate the VM
```shell
exit
```

# Documentation

[a link](https://dev.to/yahiaqous/how-to-build-a-crud-api-using-python-flask-and-sqlalchemy-orm-with-postgresql-2jjj)

Flask — це інструмент для створення вебсайтів на мові Python. Легковаговий WSGI-фреймворк (Web Server Gateway Interface). Допомагає серверу спілкуватися з сайтом, має просту структуру, вбудований сервер для тестування і зручний режим для пошуку помилок.

ORM (Object-Relational Mapping) — це технологія, яка допомагає програмістам працювати з базами даних у вигляді звичних об’єктів замість написання складних SQL-запитів. ORM автоматично переводить дані з бази (рядки, таблиці) у об’єкти в програмі, і навпаки — об’єкти у базу.

SQLAlchemy — це бібліотека, яка забезпечує зручний спосіб взаємодії з базами даних та полегшує зв’язок між програмами на Python і базами даних. Бібліотеку використовують як ORM, яка перетворює класи Python у таблиці реляційних баз даних і автоматично переводить виклики функцій у SQL-запити.

