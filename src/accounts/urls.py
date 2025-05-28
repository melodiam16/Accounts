# Імпортуємо об'єкт request для роботи з HTTP-запитами
from flask import request

# Імпортуємо об'єкт Flask-додатку
from ..app import app

# Імпортуємо контролери для обробки операцій над акаунтами
from .controllers import (
    list_all_accounts_controller,
    create_account_controller,
    retrieve_account_controller,
    update_account_controller,
    delete_account_controller
)


# Маршрут для отримання списку всіх акаунтів або створення нового акаунта
@app.route("/accounts", methods=['GET', 'POST'])
def list_create_accounts():
    # Якщо метод GET — повертаємо список акаунтів
    if request.method == 'GET':
        return list_all_accounts_controller()

    # Якщо метод POST — створюємо новий акаунт
    if request.method == 'POST':
        return create_account_controller()

    # Якщо метод не підтримується — повертаємо повідомлення
    else:
        return 'Method is Not Allowed'


# Маршрут для отримання, оновлення або видалення акаунта за ID
@app.route("/accounts/<account_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_accounts(account_id):
    # Якщо метод GET — повертаємо акаунт за ID
    if request.method == 'GET':
        return retrieve_account_controller(account_id)

    # Якщо метод PUT — оновлюємо акаунт за ID
    if request.method == 'PUT':
        return update_account_controller(account_id)

    # Якщо метод DELETE — видаляємо акаунт за ID
    if request.method == 'DELETE':
        return delete_account_controller(account_id)

    # Якщо метод не підтримується — повертаємо повідомлення
    else:
        return 'Method is Not Allowed'
