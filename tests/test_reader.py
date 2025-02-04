from unittest.mock import mock_open, patch

import pandas as pd

from src.reader import read_transact_csv, read_transact_excel


@patch("src.reader.pd.read_excel")
def test_read_transact_excel(mock_transact_excel):
    mock_transact_excel.return_value = pd.DataFrame(
        [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]
    )
    assert read_transact_excel("dir_transactions") == [
        {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}
    ]


def test_read_transact_csv():
    mock_data = "id;state;date;amount;currency_name;currency_code;from;to;description\n1;2;3;4;5;6;7;8;9\n"
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
        res = read_transact_csv("fake")
        assert res == [
            {
                "id": "1",
                "state": "2",
                "date": "3",
                "amount": "4",
                "currency_name": "5",
                "currency_code": "6",
                "from": "7",
                "to": "8",
                "description": "9",
            }
        ]
