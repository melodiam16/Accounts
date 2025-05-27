# Імпортуємо бібліотеки для роботи зі змінними середовища та шляхами
from dotenv import load_dotenv       # для завантаження змінних із .env
from pathlib import Path             # для зручної роботи з файловою системою
import os                            # для доступу до змінних середовища

# Визначаємо шлях до файлу .env у папці src/
env_path = Path(__file__).parent / ".env"

# Завантажуємо змінні середовища з .env файлу
load_dotenv(dotenv_path=env_path)

# Виводимо значення змінної середовища (для перевірки)
print("ENV VAR:", os.getenv("DEVELOPMENT_DATABASE_URL"))

from flask import Flask                      # основний клас Flask-додатку
from flask_sqlalchemy import SQLAlchemy      # ORM для бази даних
from flask_migrate import Migrate            # міграції бази даних
from .config import config                   # словник з класами конфігурацій

# Створюємо екземпляри розширень
db = SQLAlchemy()
migrate = Migrate()

# Фабрична функція створення та налаштування Flask-додатку
def create_app(config_mode):
    app = Flask(__name__)  # створюємо Flask-додаток

    # Завантажуємо конфігурацію з класу, відповідного режиму (наприклад, DevelopmentConfig)
    app.config.from_object(config[config_mode])

    # Виводимо поточний URI до бази даних (для перевірки)
    print("DB URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))

    # Ініціалізуємо SQLAlchemy з додатком
    db.init_app(app)

    # Ініціалізуємо Flask-Migrate для керування міграціями
    migrate.init_app(app, db)

    # Повертаємо налаштований додаток
    return app
