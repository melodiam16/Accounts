# Flask-інструменти для роботи з HTTP-запитами і JSON-відповідями
from flask import request, jsonify

# Модуль для генерації унікальних ідентифікаторів
import uuid

# Об'єкт бази даних
from .. import db

# Модель акаунта
from .models import Account


# Функція для отримання всіх акаунтів
def list_all_accounts_controller():
    # Отримуємо всі акаунти з бази даних
    accounts = Account.query.all()

    # Формуємо список словників акаунтів
    response = []
    for account in accounts:
        response.append(account.toDict())

    # Повертаємо список акаунтів у форматі JSON
    return jsonify(response)


# Функція для створення нового акаунта
def create_account_controller():
    # Отримуємо дані з форми запиту у вигляді словника
    request_form = request.form.to_dict()

    # Генеруємо унікальний ідентифікатор для нового акаунта
    id = str(uuid.uuid4())

    # Створюємо об'єкт акаунта з даними з форми
    new_account = Account(
        id=id,
        email=request_form['email'],
        username=request_form['username'],
        dob=request_form['dob'],
        country=request_form['country'],
        phone_number=request_form['phone_number'],
    )

    # Додаємо новий акаунт до сесії бази даних
    db.session.add(new_account)

    # Зберігаємо зміни у базі даних
    db.session.commit()

    # Отримуємо створений акаунт з бази даних і повертаємо його як JSON
    response = Account.query.get(id).toDict()
    return jsonify(response)


# Функція для отримання одного акаунта за його ID
def retrieve_account_controller(account_id):
    # Отримуємо акаунт з бази даних і повертаємо його як JSON
    response = Account.query.get(account_id).toDict()
    return jsonify(response)


# Функція для оновлення акаунта
def update_account_controller(account_id):
    # Отримуємо дані з форми запиту
    request_form = request.form.to_dict()

    # Отримуємо об'єкт акаунта за ID
    account = Account.query.get(account_id)

    # Оновлюємо поля акаунта новими значеннями
    account.email = request_form['email']
    account.username = request_form['username']
    account.dob = request_form['dob']
    account.country = request_form['country']
    account.phone_number = request_form['phone_number']

    # Зберігаємо зміни у базі даних
    db.session.commit()

    # Повертаємо оновлений акаунт як JSON
    response = Account.query.get(account_id).toDict()
    return jsonify(response)


# Функція для видалення акаунта
def delete_account_controller(account_id):
    # Видаляємо акаунт з бази даних за ID
    Account.query.filter_by(id=account_id).delete()

    # Зберігаємо зміни у базі даних
    db.session.commit()

    # Повертаємо повідомлення про успішне видалення
    return ('Account with Id "{}" deleted successfully!').format(account_id)

