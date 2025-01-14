import json
from json import JSONDecodeError

from external_api import currency_conversion


def transactions(path):
    """Функция принимает путь JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        with open(path, encoding='utf-8') as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError:
                print("Ошибка декодирования")
                return []
        return data_json
    except FileNotFoundError:
        print("Файл не найден")
        return []


def transaction_amount(transaction, currency="RUB"):
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    if transaction["operationAmount"]["currency"]["code"] == currency:
        amount = transaction["operationAmount"]["amount"]
    else:
        amount = currency_conversion(transaction)
    return f"{amount} руб"


if __name__ == "__main__":
    path = "..//data/operations.json"
    print(transactions(path))
    data = transactions(path)
    transaction_amount(data[0], "RUB")
    print(transaction_amount(data[0], "RUB"))
