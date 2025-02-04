import unittest
from unittest.mock import patch

from src.main import get_valid_status, mask_card_number, print_operations


class TestMain(unittest.TestCase):
    def test_get_valid_status(self):
        with patch("builtins.input", side_effect=["test", "EXECUTED"]):
            status = get_valid_status()
            self.assertEqual(status, "EXECUTED")

    def test_mask_card_number(self):
        # Тест для карты
        card_number = "1234 5678 9012 3456"
        masked = mask_card_number(card_number)
        self.assertEqual(masked, "1234 5678 9012 3456")

        # Тест для счета
        account_number = "Счет 1234567890123456"
        masked = mask_card_number(account_number)
        self.assertEqual(masked, "Счет **3456")

    def test_print_operations(self):
        operations = [
            {
                "date": "01.01.2023",
                "description": "Test",
                "from": "1234 5678 9012 3456",
                "to": "Счет 1234567890",
                "amount": 100,
                "currency": "RUB",
            }
        ]
        with patch("builtins.print") as mock_print:
            print_operations(operations)
            mock_print.assert_called_with("01.01.2023 Test\n1234 5678 9012 3456 -> Счет **7890\nСумма: 100 RUB\n")


if __name__ == "__main__":
    unittest.main()
