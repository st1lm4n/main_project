from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    unmask_number = str(card_number)
    counter = 0
    new_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    if len(unmask_number) == 16:
        return unmask_number[:4] + " " + "** ****" + unmask_number[-4:]
    else:
        for i in unmask_number:
            if i in new_list:
                counter += 1

    if counter != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked_number = unmask_number[0:-17] + " " + unmask_number[-16:-12] + " " + unmask_number[-12:-10] + "** ****" + " " + unmask_number[-4:]
    return masked_number



def get_mask_account(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""

    unmask_account = str(card_number)
    counter = 0
    new_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    for i in unmask_account:
        if i in new_list:
            counter += 1

    if counter != 20:
        raise ValueError("Номер счета должен состоять из 20 цифр")

    masked_account = unmask_account[:4] + " " + "**" + unmask_account[-4:]
    return masked_account

