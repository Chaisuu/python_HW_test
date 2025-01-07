import csv
import os
from typing import Any


def reader_csv(path: str) -> list[Any]:
    """" Функция считывания транзакций c файла csv, который выдает список словарей с транзакцией """
    try:
        with open(path, "r", encoding="utf-8") as file:
            csv_data = csv.DictReader(file, delimiter=";")
            return [row for row in csv_data]      # Собираем строки в список
        #        csv_data = pd.read_csv(file, delimiter=";")
    except Exception:
        return []

if __name__ == '__main__':
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
    print(reader_csv(PATH_TO_FILE))
