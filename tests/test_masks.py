import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "7365 **4305"

def test_form_get_mask_account():
    assert get_mask_account(73654108430135874305) == "7365 **4305"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(736541084301358743051)
    assert str(exc_info.value) == "Номер счета должен состоять из 20 цифр"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(7365410843013587430)
    assert str(exc_info.value) == "Номер счета должен состоять из 20 цифр"


def test_empty_get_mask_account():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Номер счета должен состоять из 20 цифр"


def test_get_mask_card_number():
    assert get_mask_card_number("7158300734726758") == "7158 ** ****6758"

def test_form_get_mask_card_number():
    assert get_mask_card_number(7158300734726758) == "7158 ** ****6758"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(71583007347267581)
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(715830073472675)
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"

def test_empty_get_mask_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"

