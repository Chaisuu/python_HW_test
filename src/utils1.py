import json
import os

from json import JSONDecodeError
from typing import Any
from src.external_api import get_amount_convert


def get_read_json(path: str) -> list[Any] | Any:
    """Функция которя принимает путь на вход и возрващает список словарей с данными о транзакциях"""

    try:
        """Eсли файл пустой, содержит не список или не найден, функция возвращает пустой список"""
        with open(path, 'r', encoding="utf-8") as f:
            try:
                transactions = json.load(f)
            except JSONDecodeError:
                return []
            else:
                return transactions
    except FileNotFoundError:
        return []
    else:
        return transactions


def get_amount_transactions(transac: list) -> Any:
    """Функция которая принимает на вход транзакцию и возращает сумму в рублях """
    currency = 'RUB'
    if transac["operationAmount"]["currency"]["code"] == currency:
        amount = transac["operationAmount"]["amount"]
    else:
        amount = get_amount_convert(transac)
    return amount


#if __name__ == '__main__':
#    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#    print(get_read_json(PATH_TO_FILE))

#transac = {
#    'id': 879660146, 'state': 'EXECUTED', 'date': '2018-07-22T07:42:32.953324',
#    'operationAmount': {'amount': '92130.50', 'currency': {'name': 'USD', 'code': 'USD'}},
#    'description': 'Перевод организации', 'from': 'Счет 19628854383215954147',
#    'to': 'Счет 90887717138446397473'}
#print(get_amount_transactions(transac))

#    transac = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
#                 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#                 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
#                 'to': 'Счет 64686473678894779589'}