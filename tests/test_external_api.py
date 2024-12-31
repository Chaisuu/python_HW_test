from unittest.mock import patch

import pytest

from src.external_api import get_amount_convert

@pytest.fixture
def trans_2():
    return{
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


@patch('requests.get')
def test_get_amount_convert(mock_get, trans_2):
    mock_get.return_value.json.return_value = {'success': True, 'query':
                                               {'from': 'USD', 'to': 'RUB', 'amount': 92130.5}, 'info':
                                               {'timestamp': 1715103603, 'rate': 1.4754},
                                               'date': '2025-01-01', 'result': 10180244.465006}
    assert get_amount_convert(trans_2) == 10180244.465006