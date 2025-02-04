import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("tests/logs/masks.log", "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    logger.info("Начало работы функции маскировки номера карты")
    unmask_number = str(card_number)
    counter = 0
    new_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    logger.info("Обработка номера карты")
    if len(unmask_number) == 16:

        return unmask_number[:4] + " " + "** ****" + unmask_number[-4:]
    else:
        for i in unmask_number:
            if i in new_list:
                counter += 1

    if counter != 16:
        logger.error(f"Произошла ошибка: {ValueError('Номер карты должен состоять из 16 цифр')}")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked_number = (
        unmask_number[0:-17]
        + " "
        + unmask_number[-16:-12]
        + " "
        + unmask_number[-12:-10]
        + "** ****"
        + " "
        + unmask_number[-4:]
    )
    logger.info("Возврат замаскированного номера карты")
    return masked_number


def get_mask_account(card_number: Union[int, str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""

    logger.info("Начало работы функции маскировки номера счета")
    unmask_account = str(card_number)
    counter = 0
    new_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    logger.info("Обработка номера счета")
    for i in unmask_account:
        if i in new_list:
            counter += 1

    if counter != 20:
        logger.error(f"Произошла ошибка: {ValueError('Номер счета должен состоять из 20 цифр')}")
        raise ValueError("Номер счета должен состоять из 20 цифр")

    masked_account = unmask_account[:4] + " " + "**" + unmask_account[-4:]
    logger.info("Возврат замаскированного номера счета")
    return masked_account


# if __name__ == "__main__":
#     print(get_mask_account(73654108430135874305))
#     print(get_mask_card_number(7158300734726758))
