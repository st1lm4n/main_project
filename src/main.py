from datetime import datetime
from typing import Any, Dict, List

from src.processing import filter_operations_by_description
from src.reader import read_csv, read_json, read_xlsx  # Импорт из reader.py


def get_valid_status() -> str:
    """Запрашивает статус операции у пользователя и валидирует его."""
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input("Введите статус операции: ").upper()
        if status in valid_statuses:
            return status
        print(f"Статус '{status}' недоступен. Доступные статусы: {', '.join(valid_statuses)}")


def mask_card_number(number: str) -> str:
    """Маскирует номер карты/счета."""
    if "Счет" in number:
        return "Счет **" + number[-4:]
    parts = number.split(" ")
    if len(parts[-1]) == 16 and parts[-1].isdigit():
        return " ".join(parts[:-1]) + " " + parts[-1][:4] + " **" + parts[-1][-4:]
    return number


def print_operations(operations: List[Dict[str, Any]]) -> None:
    """Выводит отформатированный список операций."""
    if not operations:
        print("Не найдено ни одной транзакции.")
        return
    for op in operations:
        date = datetime.strptime(op["date"], "%d.%m.%Y").strftime("%d.%m.%Y")
        desc = op["description"]
        from_account = mask_card_number(op.get("from", ""))
        to_account = mask_card_number(op.get("to", ""))
        amount = f"{op['amount']} {op['currency']}"
        print(f"{date} {desc}\n{from_account} -> {to_account}\nСумма: {amount}\n")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор файла
    file_type = input("Выберите тип файла (1-JSON, 2-CSV, 3-XLSX): ")
    file_reader = {"1": read_json, "2": read_csv, "3": read_xlsx}.get(file_type, lambda _: [])

    operations = file_reader("operations.json")

    # Фильтрация по статусу
    status = get_valid_status()
    operations = [op for op in operations if op.get("status", "").upper() == status]

    # Дополнительные фильтры
    sort_date = input("Отсортировать по дате? (Да/Нет): ").lower() == "да"
    if sort_date:
        reverse = input("По возрастанию или убыванию? (возрастания/убывания): ").lower() == "убывания"
        operations.sort(key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"), reverse=reverse)

    rub_only = input("Только рублевые транзакции? (Да/Нет): ").lower() == "да"
    if rub_only:
        operations = [op for op in operations if op.get("currency") == "RUB"]

    filter_word = input("Фильтровать по слову в описании? (Да/Нет): ").lower() == "да"
    if filter_word:
        search_word = input("Введите слово для поиска: ")
        operations = filter_operations_by_description(operations, search_word)

    print_operations(operations)


if __name__ == "__main__":
    main()
