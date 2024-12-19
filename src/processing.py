from typing import Union


def filter_by_state(list_dict: list[dict], state: str = "CANCELED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
 соответствует указанному значению"""

    new_list_dict = []

    for dict_ in list_dict:
        if dict_["state"] == state:
            new_list_dict.append(dict_)
    return new_list_dict


