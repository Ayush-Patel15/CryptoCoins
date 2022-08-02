import requests
import json
from pprint import pprint

BASE_URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

def get_crypto_list():
    session = requests.session()
    headers = {
        "authority" : "api.coinmarketcap.com",
        "method" : "GET",
        "scheme" : "https",
        "accept" : "application/json, text/plain, */*",
        "accept-encoding" : "gzip, deflate, br",
        "accept-language" : "en-US,en;q=0.9,hi;q=0.8",
        "cache-control" : "no-cache",
        "origin" : "https://coinmarketcap.com",
        "pragma" : "no-cache",
        "referer" : "https://coinmarketcap.com/",
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    para_ditc = {
        "start": "1",
        "limit": "12",
        "sortBy": "market_cap",
        "sortType" : "desc",
        "convert" : "USD",
        "aux" : "ath,atl,high24h,low24h,cmcrank,total_supply"
    }

    response = session.get(
        BASE_URL,
        headers=headers,
        params=para_ditc
    ).text
    json_data = json.loads(response)["data"]["cryptoCurrencyList"]

    pprint(len(json_data))

if __name__ == "__main__":
    get_crypto_list()