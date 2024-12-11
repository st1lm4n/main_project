from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    unmask_number = str(card_number)
    masked_number = card_number[0:-12] + " " + "** ****" + card_number[-4:]

    return masked_number


def get_mask_account(account: Union[int, str]) -> Union[str]:
    """Функцию маскировки номера банковского счета"""

    unmask_account = str(account)
    masked_account = account[:4] + " " + "**" + account[-4:]
    return masked_account
