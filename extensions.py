import json
import requests
from config import keys

class APIException(Exception):
    pass


class CriptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Нельзя перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(
                f'Не удалось обработать валюту {quote}. Доступны следующие валюты: {", ".join(keys.keys())}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(
                f'Не удалось обработать валюту {base}. Доступны следующие валюты: {", ".join(keys.keys())}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(response.content)[keys[base]]

        return total_base