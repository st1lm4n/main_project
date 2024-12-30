from typing import Iterator, Union


def filter_by_currency(lst: list[dict], key: str) -> Union[Iterator[dict], str]:
    """
    Функция которая принимает на вход список словарей и возвращает итератор,
    который поочерёдно выдает транзакции, где валюта соответствует заданной
    """

    if lst == []:
        return iter([])

    for transaction in lst:
        if transaction["operationAmount"]["currency"]["code"] == key:
            yield transaction
        else:
            return iter([])

    return iter([])


# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#    print(next(usd_transactions))


def transaction_descriptions(lst: list[dict]) -> Iterator:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """
    for x in lst:
        yield x.get("description")


# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
# print(next(descriptions))


def card_number_generator(
    start: Union[int],
    stop: Union[int],
) -> Iterator:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""

    for number in range(start, stop):
        number_card = str(number)
        while len(number_card) < 16:
            number_card = "0" + number_card
        formated_card_number = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:16]}"
        yield formated_card_number


for card_number in card_number_generator(1, 5):
    print(card_number)
