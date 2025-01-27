import csv

import pandas as pd


def read_transact_excel(dir_transact):
    """
    Функция для считывания транзакций из Excel
    """
    excel_data = pd.read_excel("..//data/transactions_excel.xlsx")
    excel_data_dict = excel_data.to_dict(orient="records")
    return excel_data_dict


# print(read_transact_excel("..//data/transactions_excel.xlsx"))


def read_transact_csv(dir_transaction):
    """
    Функция для считывания транзакций из CSV
    """
    result_dict = []

    with open(dir_transaction, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            result_dict.append(
                {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "amount": row["amount"],
                    "currency_name": row["currency_name"],
                    "currency_code": row["currency_code"],
                    "from": row["from"],
                    "to": row["to"],
                    "description": row["description"],
                }
            )
    return result_dict


print(read_transact_csv("data/test_transaction.csv"))


# read_transact_exel("..//data/transactions_excel.xlsx")
