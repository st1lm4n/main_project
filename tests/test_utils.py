from unittest.mock import patch

from src.utils import transaction_amount, transactions

path = "data/operations.json"
data = transactions(path)


def test_transaction(transact):
    assert transactions(path) == transact


def test_invalid_transaction():
    assert transactions("") == []


def test_empty_transaction_():
    assert transactions("..//data/op.json") == []


def test_invalid_transaction_():
    assert transactions("..//data/op.json") == []


def test_transaction_amount():
    assert transaction_amount(data[3], "RUB") == "48223.05"


@patch("requests.request")
def test_transaction_amount_rub(mock_get):
    mock_get.return_value = {"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}
    assert transaction_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1


@patch("requests.request")
def test_transaction_amount_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 1.00}
    assert transaction_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1
