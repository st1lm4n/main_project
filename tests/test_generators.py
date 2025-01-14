import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    i = filter_by_currency(transactions, "USD")
    assert next(i) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }, {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_empty():
    i = filter_by_currency([], "USD")
    assert list(i) == []


def test_filter_by_currency_invalid_key(transactions: list[dict]):
    i = filter_by_currency(transactions, "CY")
    assert list(i) == []


def test_transaction_descriptions(transactions):
    i = transaction_descriptions(transactions)
    assert next(i) == "Перевод организации"
    assert next(i) == "Перевод со счета на счет"
    assert next(i) == "Перевод со счета на счет"
    assert next(i) == "Перевод с карты на карту"
    assert next(i) == "Перевод организации"


def test_transaction_descriptions_empty():
    i = transaction_descriptions([])
    assert list(i) == []


def test_card_number_generator():
    i = card_number_generator(1, 2)
    assert next(i) == "0000 0000 0000 0001"


@pytest.mark.parametrize("start, stop, expected", [(100, 101, ("0000 0000 0000 0100"))])
def test_card_number_generator_else(start, stop, expected):
    assert next(card_number_generator(start, stop)) == expected


def test_card_number_generator_fin():
    i = card_number_generator(9999999999999998, 10000000000000000)
    assert next(i) == "9999 9999 9999 9998"
    assert next(i) == "9999 9999 9999 9999"
