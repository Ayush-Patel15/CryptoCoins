"""
The file contains a function, that scrapes the data of top 12 cryptocurrencies by market cap.
Data contains: -
- name
- price
- days_high
- days_low
- ath
- atl
- total_supply
- market_cap
- volume
- change of price in last 1hr (percent)
- yeartodate price change percent
"""
## Import Statements
# from pprint import pprint
from .user_agents import USER_AGENTS
from .helpers import _get_json_, round_number
import random

# BASE_URLS
COINMARKETCAP_LIST_URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

# HEADERS
coinmarketcap_headers = {
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
    "user-agent" : random.choice(USER_AGENTS)
}


##########  FUNCTIONS  ##########

# Function scrape the COINMARKETCAP's URL to get basic details like price, name etc.
# It returns list of 12 cryptocurrencies.
def get_cryptocurrency_list():
    crypto_list = []
    para_dict = {
        "start": "1",
        "limit": "12",
        "sortBy": "market_cap",
        "sortType" : "desc",
        "convert" : "USD",
        "aux" : "ath,atl,high24h,low24h,cmcrank,total_supply"
    }
    response = _get_json_(
        url=COINMARKETCAP_LIST_URL,
        headers=coinmarketcap_headers,
        params=para_dict
    )
    list_data = response["data"]["cryptoCurrencyList"]
    for each in list_data:
        quotes_data = each["quotes"][0]
        item = {
            "identifier": each["symbol"],
            "slug": each["slug"],
            "data": {
                "name": each["name"].upper(),
                "day_high": round_number(each["high24h"]),
                "day_low": round_number(each["low24h"]),
                "ath": round_number(each["ath"]),
                "atl": round_number(each["atl"]),
                "total_sypply": round_number(each["totalSupply"]),
                "price": round_number(quotes_data["price"]),
                "market_cap": round_number(quotes_data["marketCap"]),
                "volume": round_number(quotes_data["volume24h"]),
                "change_1hr": round_number(quotes_data["percentChange1h"]),
                "ytd_change": round_number(quotes_data["ytdPriceChangePercentage"])
            }
        }
        crypto_list.append(item)
    return crypto_list
    

if __name__ == "__main__":
    print(get_cryptocurrency_list())