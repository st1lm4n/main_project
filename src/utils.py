import json
import logging
from json import JSONDecodeError

from src.external_api import currency_conversion

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def transactions(path):
    """Функция принимает путь JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        logger.info("Открытие JSON-файла по заданному пути")
        with open(path, encoding="utf-8") as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError as ex:
                logger.error(f"Произошла ошибка: {ex}")
                print("Ошибка декодирования")
                return []
        logger.info("Возврат списка транзакций")
        return data_json
    except FileNotFoundError as exc:
        logger.error(f"Произошла ошибка: {exc}")
        print("Файл не найден")
        return []


def transaction_amount(transaction, currency="RUB"):
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    logger.info("Транзакция принята в обработку")
    if transaction["operationAmount"]["currency"]["code"] == currency:
        logger.info("Проверка валюты транзакции")
        amount = transaction["operationAmount"]["amount"]
    else:
        amount = currency_conversion(transaction)
    logger.info("Возврат суммы транзакции")
    return amount


if __name__ == "__main__":
    path = "..//data/operations.json"
    print(transactions(path))
    data = transactions(path)
    transaction_amount(data[0], "RUB")
    print(transaction_amount(data[0], "RUB"))
