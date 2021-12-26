import requests
import os

price_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
metadata_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv("coinsKey", None)
}
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}


def get_all_coins_price():
    json = requests.get(price_url, params=parameters, headers=headers).json()
    coins = json['data']
    data = []
    for row in coins:
        row_data = []
        row_data.append(row['name'])
        row_data.append(row['symbol'])
        row_data.append(row['quote']['USD']['price'])
        row_data.append(row['quote']['USD']['percent_change_1h'])
        row_data.append(row['quote']['USD']['percent_change_24h'])
        row_data.append(row['quote']['USD']['percent_change_7d'])
        row_data.append(row['quote']['USD']['percent_change_30d'])
        data.append(row_data)
    return data


def get_all_coins_metadata():
    json = requests.get(price_url, params=parameters, headers=headers).json()
    coins = json['data']
    data = []
    for row in coins:
        row_data = []
        row_data.append(row['data']['1']['name'])
        row_data.append(row['data']['1']['symbol'])
        row_data.append(row['data']['1']['logo'])
        row_data.append(row['data']['1']['urls']['website'])
        row_data.append(row['data']['1']['urls']['technical_doc'])
        data.append(row_data)
    return data


def get_coin_price(coin):
    coinArray = get_all_coins_price()
    for i in range(0, 100):
        if coinArray[i][1].lower == coin:
            return coinArray[i]
    return []


def get_coin_metadata(coin):
    coinArray = get_all_coins_metadata()
    for i in range(0, 100):
        if coinArray[i][1].lower == coin:
            return coinArray[i]
    return []


def check_coin(coin):
    coinArray = get_all_coins_price()
    for i in range(0, 100):
        if (coinArray[i][1].lower == coin):
            return True
    return False
