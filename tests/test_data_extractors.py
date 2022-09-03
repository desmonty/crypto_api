import json
import os
import requests
import unittest

from dotenv import load_dotenv


class TestDataExtractors(unittest.TestCase):
    def test_CoinGecko_api(self):
        url = 'https://api.coingecko.com/api/v3/ping'

        headers = {
            "accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

    def test_CoinMarketCap_api(self):
        load_dotenv()
        url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start':'1',
          'limit':'5000',
          'convert':'USD'
        }
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': os.getenv('COINMARKETCAP_API_KEY'),
        }

        response = requests.get(url, params=parameters, headers=headers)
        response.raise_for_status()

if __name__ == '__main__':
    unittest.main()
