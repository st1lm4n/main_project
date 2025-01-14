import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction):
    """Функция для конвертирования суммы транзакции в рубли"""
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={transaction["operationAmount"]["currency"]["code"]}&amount={transaction["operationAmount"]["amount"]}"

        payload = {}
        headers = {"apikey": "tdbxyBL5B83no68xyK9Vs6BvcTbZwL2m"}

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.json()
        return f"{round(result["result"], 2)} руб"
