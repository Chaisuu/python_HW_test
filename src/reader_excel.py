import os
from typing import Any

import pandas as pd


def reader_excel(path: str) -> list[Any]:
    """Функция считывания транзакций c файла excel, который выдает список словарей с транзакцией"""
    try:
        csv_data = pd.read_excel(path)
        result = csv_data.to_dict(orient='records')
        return  result
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
    print(reader_excel(PATH_TO_FILE))
