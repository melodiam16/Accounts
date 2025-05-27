 #models.py описує модель бази даних для користувацького акаунта у веб-додатку на Flask

from sqlalchemy import inspect  #допомагає динамічно отримати дані про модель
from datetime import datetime   #для роботи з датою і часом
from flask_validator import ValidateEmail, ValidateString, ValidateCountry    #пакет для валідації полів
from sqlalchemy.orm import validates   #декоратор SQLAlchemy для перевірки полів

from .. import db # from __init__.py   #це екземпляр SQLAlchemy, що зв’язаний з базою

class Account(db.Model):   #клас-модель, яка створює таблицю у базі
    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date)
    country = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))

    @classmethod
    def __declare_last__(cls):
        ValidateEmail(Account.email, True, True,"The email is not valid. Please check it")
        ValidateString(Account.username, True, True, "The username type must be string")
        ValidateCountry(Account.country, True, True, "The country is not valid")


    @validates('username')
    def empty_string_to_null(self, key, value):   #self - об'єкт    key - назва   value - значення
        if isinstance(value, str) and value == '':
            return None
        else:
            return value


    def toDict(self):   #робить об'єкт словником
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):   #визначає, як виглядає об'єкт
        return "<%r>" % self.email   #виводить рядок у лапках


# Імпортує модулі
# Оголошує модель Account
# Визначає поля таблиці
# Додає валідацію полів
# Обробляє порожній username
# Перетворює об’єкт на словник
# Визначає рядкове представлення об’єкта