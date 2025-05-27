#Мета файлу config.py — відокремити налаштування додатку від коду

#доступу до змінних середовища
import os

#Config - базовий клас, від якого наслідуються всі інші конфігурації
class Config:
    #вмикає відстеження змін в об'єктах SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = True
class DevelopmentConfig(Config):
    DEVELOPMENT = True  #для локального розроблення
    DEBUG = True        #щоб бачити помилки
    #URI для бази даних береться з змінної середовища DEVELOPMENT_DATABASE_URL
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")

class TestingConfig(Config):
    TESTING = True    #вмикає спеціальні тести
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("STAGING_DATABASE_URL")

class ProductionConfig(Config):
    DEBUG = False   # не можна показувати помилки користувачам
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}