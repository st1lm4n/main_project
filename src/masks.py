from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""

    unmask_number = str(card_number)

    return f"{unmask_number[:4]} {unmask_number[4:6]}** **** {unmask_number[-4:]}"


def get_mask_account(account: Union[int, str]) -> str:
    """Функцию маскировки номера банковского счета"""

    unmask_account = str(account)

    return f"**{unmask_account[-4:]}"
