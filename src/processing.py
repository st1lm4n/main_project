from typing import Union

from tests.conftest import my_dict


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

