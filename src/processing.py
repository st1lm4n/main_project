import re
from typing import Any, Dict, List, Union


def filter_by_state(list_dict: list[dict], state: str = "CANCELED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""

    new_list_dict = []

    for dict_ in list_dict:
        if dict_["state"] == state:
            new_list_dict.append(dict_)
    return new_list_dict


def filter_by_date(
    list_dict: list[dict[str, Union[str, int]]], revers_: bool = True
) -> list[dict[str, Union[str, int]]]:
    """Функция сортировки по дате"""

    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=revers_)

    return sorted_list


def filter_operations_by_description(operations: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Фильтрует операции по строке в описании с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [op for op in operations if pattern.search(op.get("description", ""))]


def count_operations_by_category(operations: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Считает количество операций по заданным категориям."""
    category_counts = {category: 0 for category in categories}
    for op in operations:
        category = op.get("description")
        if category in category_counts:
            category_counts[category] += 1
    return category_counts
