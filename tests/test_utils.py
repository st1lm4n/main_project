import json
import os
import unittest
from unittest.mock import patch

from src.utils import transaction_amount, transactions


class TestUtils(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый JSON-файл
        self.test_json_path = "test_operations.json"
        self.test_data = [
            {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}},
            {"operationAmount": {"amount": 200, "currency": {"code": "USD"}}},
        ]
        with open(self.test_json_path, "w", encoding="utf-8") as f:
            json.dump(self.test_data, f)

        # Создаем тестовый лог-файл
        self.log_path = "../tests/logs/utils.log"
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        with open(self.log_path, "w", encoding="utf-8") as f:
            f.write("")

    def test_transactions_valid_file(self):
        """Тест для корректного JSON-файла."""
        result = transactions(self.test_json_path)
        self.assertEqual(result, self.test_data)

    def test_transactions_invalid_file(self):
        """Тест для некорректного JSON-файла."""
        invalid_json_path = "invalid_operations.json"
        with open(invalid_json_path, "w", encoding="utf-8") as f:
            f.write("invalid json")
        result = transactions(invalid_json_path)
        self.assertEqual(result, [])
        os.remove(invalid_json_path)

    def test_transactions_file_not_found(self):
        """Тест для случая, когда файл не найден."""
        result = transactions("non_existent_file.json")
        self.assertEqual(result, [])

    @patch("src.utils.currency_conversion")
    def test_transaction_amount_rub(self, mock_currency_conversion):
        """Тест для суммы транзакции в рублях."""
        transaction = self.test_data[0]
        result = transaction_amount(transaction, "RUB")
        self.assertEqual(result, 100)
        mock_currency_conversion.assert_not_called()

    @patch("src.utils.currency_conversion")
    def test_transaction_amount_usd(self, mock_currency_conversion):
        """Тест для суммы транзакции в другой валюте."""
        mock_currency_conversion.return_value = 15000  # Мок конвертации
        transaction = self.test_data[1]
        result = transaction_amount(transaction, "RUB")
        self.assertEqual(result, 15000)
        mock_currency_conversion.assert_called_once_with(transaction)


if __name__ == "__main__":
    unittest.main()
