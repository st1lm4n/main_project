import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


@pytest.mark.parametrize(
    "number_card, expected",
    [("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"), ("Счет 89701605943211234567", "Счет **4567")],
)
def test_mask_account_card_(number_card, expected):
    assert mask_account_card(number_card) == expected


def test_mask_invalid_account_card(number_card):
    with pytest.raises(ValueError):
        mask_account_card("Счет 8970605943211234567")


@pytest.fixture
def date():
    return ["2024-03-11T02:26:18.671407", "2024-12-31"]


@pytest.mark.parametrize(
    "date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-12-31", "31.12.2024")]
)
def test_get_date(date, expected):
    assert get_date(date) == expected
