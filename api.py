import requests
import os

price_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
metadata_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv("coinsKey", None)
}


def get_all_coins_price():
    parameters = {
        'start': '1',
        'limit': '100',
        'convert': 'USD'
    }
    json = requests.get(price_url, params=parameters, headers=headers).json()
    coins = json['data']
    data = []
    for row in coins:
        row_data = []
        row_data.append(row['name'])
        row_data.append(row['symbol'])
        row_data.append(round(row['quote']['USD']['price'], 2))
        row_data.append(round(row['quote']['USD']['market_cap']))
        row_data.append(round(row['quote']['USD']['volume_24h']))
        row_data.append(round(row['quote']['USD']['percent_change_1h'], 4))
        row_data.append(round(row['quote']['USD']['percent_change_24h'], 4))
        row_data.append(round(row['quote']['USD']['percent_change_7d'], 4))
        row_data.append(round(row['quote']['USD']['percent_change_30d'], 4))
        data.append(row_data)
    return data


def get_coin_metadata(coin):
    parameters_metadata = {
        "symbol": coin
    }
    json = requests.get(metadata_url, params=parameters_metadata, headers=headers).json()
    coin_data = json['data'][coin.upper()]
    data = []
    data.append(coin_data['name'])
    data.append(coin_data['symbol'])
    data.append(coin_data['logo'])
    data.append(coin_data['urls']['website'])
    data.append(coin_data['urls']['technical_doc'])
    return data


def get_coin_price(coin):
    coinArray = get_all_coins_price()
    for i in range(0, 100):
        if coinArray[i][1].lower == coin:
            return coinArray[i]
    return []


def check_coin(coin):
    coinArray = get_all_coins_price()
    for i in range(0, 100):
        if coinArray[i][1].lower == coin:
            return True
    return False
