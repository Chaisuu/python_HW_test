import os
from unittest.mock import patch, Mock

import pytest

from src.utils1 import get_read_json, get_amount_transactions
from src.external_api import get_amount_convert



@pytest.fixture
def path():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path_empty_list():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_1.json")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_2.json")
    return PATH_TO_FILE


@pytest.fixture
def trans_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
         "amount": "31957.58",
         "currency": {
          "name": "руб.",
          "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


@pytest.fixture
def trans_2():
    return {
    "id": 879660146,
    "state": "EXECUTED",
    "date": "2018-07-22T07:42:32.953324",
    "operationAmount": {
      "amount": "92130.50",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 19628854383215954147",
    "to": "Счет 90887717138446397473"}


def test_get_read_json(path):
    assert get_read_json(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
             "name": "руб.",
             "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}

def test_get_read_json_empty(path_empty_list):
    assert get_read_json(path_empty_list) == []

def test_get_read_json_mistake(path_mistake_json):
    assert get_read_json(path_mistake_json) == []

def test_get_amount_transactions(trans_1):
    assert get_amount_transactions(trans_1) == '31957.58'

@patch('src.utils1.get_amount_convert')
def test_get_amount_transactions_USD_EUR(mock_amount_convert, trans_2):
    mock_amount_convert.return_value = 10144.4
    assert get_amount_transactions(trans_2) == 10144.4




