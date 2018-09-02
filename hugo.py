import sys
import requests

def get_id(crypto_name):
    """
    Returns id of case-sensitive crypto currency name.

    None is returned if crypto name is not recognized.
    """
    url = 'https://api.coinmarketcap.com/v2/listings/'
    res = requests.get(url, headers={'Accept': 'application/json',
                                     'Accept-Encoding': 'gzip, deflate'}).json()

    for d in res['data']:
        if crypto_name == d['name']:
            return d['id']

    return None

def get_data(crypto_id):
    """
    Returns a (price, market_cap) tuple for given crypto id.
    """
    url =  f'https://api.coinmarketcap.com/v2/ticker/{crypto_id}/'
    res = requests.get(url, headers={'Accept': 'application/json',
                                     'Accept-Encoding': 'gzip, deflate'}).json()

    price = res['data']['quotes']['USD']['price']
    market_cap = res['data']['quotes']['USD']['market_cap']

    return (price, market_cap)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <crypto_currency_name>')
    else:
        crypto_name = sys.argv[1]
        crypto_id = get_id(crypto_name)

        if crypto_id is None:
            print(f"Crypto name '{crypto_name}' is not recognized by the api")
            print("Here are some recognized crypto names: 'Bitcoin', 'Ethereum'")
        else:
            price, market_cap = get_data(crypto_id)
            print(f'Price USD: {price}')
            print(f'Market Cap USD: {market_cap}')
