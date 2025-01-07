import csv
from unittest.mock import patch, mock_open
from src.reader_csv import reader_csv


def test_reader_csv_mock():
    """
    Тестирование функции проверки CSV-файла на соот-е результата ожидаемому списку словарей.
    """
    mock_read_csv = "name;amount;date\nSol;16210;2025-01-01\nPeso;29740;2025-02-02\n"
    expected_result = [
        {"name": "Sol", "amount": "16210", "date": "2025-01-01"},
        {"name": "Peso", "amount": "29740", "date": "2025-02-02"},
    ]

    with patch("builtins.open", mock_open(read_data=mock_read_csv), create=True):
        with patch("csv.DictReader", return_value=csv.DictReader(mock_read_csv.splitlines(), delimiter=";")):
            result = reader_csv("fake_file.csv")
            assert result == expected_result


def test_read_csv_invalid_path():
    """
    тестирование функции когда передан путь которого нет в директории
    """
    transactions = reader_csv("/some/path")
    assert transactions == []


def test_read_csv_not_path():
    """
    тестирование функции когда ничего не передано
    """
    transactions = reader_csv("")
    assert transactions == []
