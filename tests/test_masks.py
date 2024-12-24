from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "7365 **4305"

def test_form_get_mask_account():
    assert get_mask_account(73654108430135874305) == "7365 **4305"
    assert get_mask_account(736541084301358743051) == "Не соответствующее количество символов"
    assert get_mask_account(7365410843013587430) == "Не соответствующее количество символов"

def test_empty_get_mask_account():
    assert get_mask_account("") == "Не соответствующее количество символов"

def test_get_mask_card_number():
    assert get_mask_card_number("7158300734726758") == "7158 ** ****6758"

def test_form_get_mask_card_number():
    assert get_mask_card_number(7158300734726758) == "7158 ** ****6758"
    assert get_mask_card_number(71583007347267581) == "Не соответствующее количество символов"
    assert get_mask_card_number(715830073472675) == "Не соответствующее количество символов"

def test_empty_get_mask_card_number():
    assert get_mask_card_number("") == "Не соответствующее количество символов"

