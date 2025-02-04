import unittest

import pytest

from src.processing import (count_operations_by_category, filter_by_date, filter_by_state,
                            filter_operations_by_description)


def test_filter_by_state(my_dict: list[dict], value_key: str = "EXECUTED") -> None:
    assert filter_by_state(my_dict, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_invalid(my_dict: list[dict], value_key: str = "EXECUTED") -> None:
    assert filter_by_state(my_dict, "FROZEN") == []


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("FROZEN", []),
    ],
)
def test_filter_state(my_dict, state, expected):
    assert filter_by_state(my_dict, state) == expected


@pytest.mark.parametrize(
    "reverse_, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_filter_date(my_dict, reverse_, expected):
    filter_by_date(my_dict, reverse_) == expected


def test_filter_by_date_same(same_my_dict):
    assert filter_by_date(same_my_dict, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.operations = [
            {"description": "Покупка в магазине", "amount": 100},
            {"description": "Перевод другу", "amount": 200},
            {"description": "Оплата услуг", "amount": 300},
        ]

    def test_filter_operations_by_description(self):
        filtered = filter_operations_by_description(self.operations, "Перевод")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["description"], "Перевод другу")

    def test_count_operations_by_category(self):
        categories = ["Покупка в магазине", "Оплата услуг"]
        counts = count_operations_by_category(self.operations, categories)
        self.assertEqual(counts["Покупка в магазине"], 1)
        self.assertEqual(counts["Оплата услуг"], 1)
        self.assertNotIn("Перевод другу", counts)


if __name__ == "__main__":
    unittest.main()
