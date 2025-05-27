#Flask-інструменти для роботи з запитами і JSON
from flask import request, jsonify

#модуль для генерації унікальних ідентифікаторів
import uuid

#об'єкт бази даних
from .. import db

#модель Account
from .models import Account

# Функція для отримання всіх акаунтів
def list_all_accounts_controller():
    accounts = Account.query.all()
    response = []
    for account in accounts: response.append(account.toDict())
    return jsonify(response)

# Функція для створення нового акаунту
def create_account_controller():
    # Отримуємо дані з форми у вигляді словника
    request_form = request.form.to_dict()

    # Генеруємо унікальний ідентифікатор для нового акаунта
    id = str(uuid.uuid4())

    # Створюємо новий об'єкт акаунта з даними з форми
    new_account = Account(
        id=id,
        email=request_form['email'],
        username=request_form['username'],
        dob=request_form['dob'],
        country=request_form['country'],
        phone_number=request_form['phone_number'],
    )

    # Додаємо новий акаунт у сесію бази даних
    db.session.add(new_account)

    # Фіксуємо зміни у базі даних
    db.session.commit()

    response = Account.query.get(id).toDict()
    return jsonify(response)


def retrieve_account_controller(account_id):
    response = Account.query.get(account_id).toDict()
    return jsonify(response)


def update_account_controller(account_id):
    request_form = request.form.to_dict()
    account = Account.query.get(account_id)

    account.email = request_form['email']
    account.username = request_form['username']
    account.dob = request_form['dob']
    account.country = request_form['country']
    account.phone_number = request_form['phone_number']
    db.session.commit()

    response = Account.query.get(account_id).toDict()
    return jsonify(response)


def delete_account_controller(account_id):
    Account.query.filter_by(id=account_id).delete()
    db.session.commit()

    return ('Account with Id "{}" deleted successfully!').format(account_id)
