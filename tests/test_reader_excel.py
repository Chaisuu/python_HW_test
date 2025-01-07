from unittest.mock import patch
import pandas as pd
from src.reader_excel import reader_excel


@patch("pandas.read_excel")
def test_reader_excel(mock_read_excel):
    """
    Тестированин функции на  чтение Excel-файла и проверку на соот-е ожидаемому списку словарей
    """
    mock_data = [{"transaction_id": 650703.0, "amount": 16210.0}, {"transaction_id": 3598919.0, "amount": 29740.0}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    result = reader_excel("file.xlsx")
    assert result == mock_data


def test_reader_excel_empty():
    """
    тестирование функции когда имя файла пустое
    """
    result = reader_excel("")
    assert result == []


@patch("pandas.read_excel")
def test_reader_excel_file_not_found(mock_read_excel):
    """
    Тестирование когда файл не найден что функция возвращает пустой список
    """
    mock_read_excel.side_effect = FileNotFoundError
    result = reader_excel("file.xlsx")
    assert result == []