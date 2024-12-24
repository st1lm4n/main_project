from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    unmask_number = str(card_number)

    if 16 <= len(unmask_number) <= 16:
        masked_number = unmask_number[0:-12] + " " + "** ****" + unmask_number[-4:]
        return masked_number
    return "Не соответствующее количество символов"


def get_mask_account(account: Union[int, str]) -> Union[str]:
    """Функцию маскировки номера банковского счета"""

    unmask_account = str(account)

    if 20 <= len(unmask_account) <= 20:
        masked_account = unmask_account[:4] + " " + "**" + unmask_account[-4:]
        return masked_account
    return "Не соответствующее количество символов"

