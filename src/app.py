import os

# Завантаження змінних середовища з файлу .env
from dotenv import load_dotenv
load_dotenv()

# Ініціалізація застосунку через функцію create_app з __init__.py
from . import create_app
app = create_app(os.getenv("CONFIG_MODE"))

# ----------------------------------------------- #

# Базовий маршрут — перевірка, що застосунок працює
@app.route('/')
def hello():
    return "Hello World!"

# Імпортуємо маршрути акаунтів (автоматично додаються до app через blueprint)
from .accounts import urls

# ----------------------------------------------- #

# Точка входу при запуску напряму: python <filename>.py
if __name__ == "__main__":
    # Для запуску сервера у терміналі:
    # flask run -h localhost -p 5000

    # Для запуску сервера з автоматичним перезапуском при зміні коду:
    # FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()
