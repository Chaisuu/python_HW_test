import json
import os
from json import JSONDecodeError
from typing import Any
import logging
from src.external_api import get_amount_convert

#if not os.path.exists('logs'):
#    os.makedirs('logs')

logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('../logs/utils1.log', encoding="utf-8", mode="w")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_read_json(path: str) -> list[Any] | Any:
    """Функция которя принимает путь на вход и возрващает список словарей с данными о транзакциях"""

    try:
        with open(path, 'r', encoding="utf-8") as f:
            logger.info("pass path where file is located")
            try:
                transactions = json.load(f)
                logger.info("open file")
            except JSONDecodeError:
                logger.error("Error JSONDecode")
                return []
            else:
                return transactions
    except FileNotFoundError:
        logger.error("Error: type file not lisr or FileNotFound")
        return []
    else:
        return transactions


def get_amount_transactions(transaction: list) -> Any:
    """Функция которая принимает на вход транзакцию и возращает сумму в рублях """
    currency = 'RUB'
    logger.info("amount in RUB")
    if transaction["operationAmount"]["currency"]["code"] == currency:
        amount = transaction["operationAmount"]["amount"]
    else:
        logger.info("amount in RUB after conversion")
        amount = get_amount_convert(transaction)

    return amount


if __name__ == '__main__':
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    print(get_read_json(PATH_TO_FILE))
