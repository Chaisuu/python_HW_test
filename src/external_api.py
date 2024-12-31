import os
from typing import Any

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount_convert(transac: list) -> Any:
    amout = transac["operationAmount"]["amount"]
    code = transac["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload = {}
    response = requests.get(url, headers={"apikey": API_KEY}, data=payload)
    result = response.json()
    return result["result"]