from collections import defaultdict, namedtuple
from datetime import datetime
from typing import Any, Callable, Dict, List

from src.processing import filter_operations_by_description
from src.reader import read_csv, read_json, read_xlsx

# Определяем namedtuple для операций
Operation = namedtuple("Operation",
                       ["date", "description", "from_account", "to_account", "amount", "currency", "status"])


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


def print_operations(operations: List[Operation]) -> None:
    """Выводит отформатированный список операций."""
    if not operations:
        print("Не найдено ни одной транзакции.")
        return
    for op in operations:
        date = datetime.strptime(op.date, "%d.%m.%Y").strftime("%d.%m.%Y")
        from_account = mask_card_number(op.from_account) if op.from_account else ""
        to_account = mask_card_number(op.to_account) if op.to_account else ""
        amount = f"{op.amount} {op.currency}"
        print(f"{date} {op.description}\n{from_account} -> {to_account}\nСумма: {amount}\n")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор файла
    file_type = input("Выберите тип файла (1-JSON, 2-CSV, 3-XLSX): ")
    file_reader: Dict[str, Callable[[str], List[Dict[str, Any]]]] = {
        "1": read_json,
        "2": read_csv,
        "3": read_xlsx,
    }
    reader = file_reader.get(file_type, lambda _: [])
    operations_data = reader("..//data/operations.json")

    # Преобразуем данные в namedtuple
    operations = [
        Operation(
            date=op.get("date", ""),
            description=op.get("description", ""),
            from_account=op.get("from", ""),
            to_account=op.get("to", ""),
            amount=op.get("amount", 0),
            currency=op.get("currency", "RUB"),
            status=op.get("status", "").upper(),
        )
        for op in operations_data
    ]

    # Фильтрация по статусу
    status = get_valid_status()
    operations = [op for op in operations if op.status == status]

    # Дополнительные фильтры
    sort_date = input("Отсортировать по дате? (Да/Нет): ").lower() == "да"
    if sort_date:
        reverse = input("По возрастанию или убыванию? (возрастания/убывания): ").lower() == "убывания"
        operations.sort(key=lambda x: datetime.strptime(x.date, "%d.%m.%Y"), reverse=reverse)

    rub_only = input("Только рублевые транзакции? (Да/Нет): ").lower() == "да"
    if rub_only:
        operations = [op for op in operations if op.currency == "RUB"]

    filter_word = input("Фильтровать по слову в описании? (Да/Нет): ").lower() == "да"
    if filter_word:
        search_word = input("Введите слово для поиска: ")
        operations = [op for op in operations if filter_operations_by_description([op._asdict()], search_word)]

    print_operations(operations)


def count_operations_by_category(operations: List[Operation]) -> Dict[str, int]:
    """Подсчитывает количество операций по категориям."""
    category_counts = defaultdict(int)
    for op in operations:
        category_counts[op.description] += 1
    return category_counts


if __name__ == "__main__":
    main()
