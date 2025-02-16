import unittest
from collections import defaultdict
from typing import List, Dict
from unittest.mock import patch

from src.main import Operation
from src.main import get_valid_status, mask_card_number, print_operations
from src.main import main


class TestMain(unittest.TestCase):
    @patch("builtins.input", side_effect=["invalid", "EXECUTED"])
    def test_get_valid_status(self, mock_input):
        """Тест для функции get_valid_status."""
        result = get_valid_status()
        self.assertEqual(result, "EXECUTED")

    def test_mask_card_number(self):
        """Тест для функции mask_card_number."""
        # Тест для карты
        card_number = "1234 5678 9012 3456"
        masked = mask_card_number(card_number)
        self.assertEqual(masked, "1234 5678 9012 3456")

        # Тест для счета
        account_number = "Счет 1234567890123456"
        masked = mask_card_number(account_number)
        self.assertEqual(masked, "Счет **3456")

    def test_print_operations(self):
        """Тест для функции print_operations."""
        operations = [
            Operation(
                date="01.01.2023",
                description="Test",
                from_account="1234 5678 9012 3456",
                to_account="Счет 1234567890",
                amount=100,
                currency="RUB",
                status="EXECUTED",
            )
        ]
        with patch("builtins.print") as mock_print:
            print_operations(operations)
            mock_print.assert_called_with("01.01.2023 Test\n1234 5678 9012 3456 -> Счет **7890\nСумма: 100 RUB\n")


def count_operations_by_category(operations: List[Operation]) -> Dict[str, int]:
    """Подсчитывает количество операций по категориям."""
    category_counts = defaultdict(int)
    for op in operations:
        category_counts[op.description] += 1
    return category_counts


class TestCountOperationsByCategory(unittest.TestCase):
    def test_count_operations_by_category(self):
        """Тест для функции count_operations_by_category."""
        operations = [
            Operation(
                date="01.01.2023",
                description="Покупка",
                from_account="1234 5678 9012 3456",
                to_account="Счет 1234567890",
                amount=100,
                currency="RUB",
                status="EXECUTED",
            ),
            Operation(
                date="02.01.2023",
                description="Перевод",
                from_account="1234 5678 9012 3456",
                to_account="Счет 1234567890",
                amount=200,
                currency="RUB",
                status="EXECUTED",
            ),
            Operation(
                date="03.01.2023",
                description="Покупка",
                from_account="1234 5678 9012 3456",
                to_account="Счет 1234567890",
                amount=300,
                currency="RUB",
                status="EXECUTED",
            ),
        ]
        result = count_operations_by_category(operations)
        self.assertEqual(result, {"Покупка": 2, "Перевод": 1})


class TestMainIntegration(unittest.TestCase):
    @patch("src.main.read_json")
    @patch("src.main.get_valid_status")
    @patch("builtins.input", side_effect=["1", "EXECUTED", "нет", "нет", "нет"])
    def test_main_integration(self, mock_input, mock_get_status, mock_read_json):
        """Интеграционный тест для функции main."""
        # Мок данных
        mock_read_json.return_value = [
            {
                "date": "01.01.2023",
                "description": "Test",
                "from": "1234 5678 9012 3456",
                "to": "Счет 1234567890",
                "amount": 100,
                "currency": "RUB",
                "status": "EXECUTED",
            }
        ]
        mock_get_status.return_value = "EXECUTED"

        # Запуск main
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with("01.01.2023 Test\n1234 5678 9012 3456 -> Счет **7890\nСумма: 100 RUB\n")
