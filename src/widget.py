from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: Union[str]) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if "Счёт" and "Счет" in card_number:
        return get_mask_account(card_number)
    else:
        return get_mask_card_number(card_number)


def get_date(data_full: Union[str]) -> str:
    """Функция для преобразования даты"""

    date = data_full[8:10] + "." + data_full[5:7] + "." + data_full[:4]

    return date
