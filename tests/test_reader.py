import os
import unittest

from src.reader import read_csv, read_json, read_xlsx


class TestReader(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые файлы
        self.json_file = "test_transactions.json"
        self.csv_file = "test_transactions.csv"
        self.xlsx_file = "test_transactions.xlsx"

        # JSON
        with open(self.json_file, "w", encoding="utf-8") as f:
            f.write('[{"date": "01.01.2023", "description": "Test", "amount": 100}]')

        # CSV
        with open(self.csv_file, "w", encoding="utf-8") as f:
            f.write("date,description,amount\n01.01.2023,Test,100")

        # XLSX
        from openpyxl import Workbook

        wb = Workbook()
        ws = wb.active
        ws.append(["date", "description", "amount"])
        ws.append(["01.01.2023", "Test", 100])
        wb.save(self.xlsx_file)

    def tearDown(self):
        # Удаляем тестовые файлы
        os.remove(self.json_file)
        os.remove(self.csv_file)
        os.remove(self.xlsx_file)

    def test_read_json(self):
        data = read_json(self.json_file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["description"], "Test")

    def test_read_csv(self):
        data = read_csv(self.csv_file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["description"], "Test")

    def test_read_xlsx(self):
        data = read_xlsx(self.xlsx_file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["description"], "Test")


if __name__ == "__main__":
    unittest.main()
