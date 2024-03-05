import requests
import sys

def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

try:
    if len(sys.argv) == 2:
        if is_float(sys.argv[1]):
            # No. of Bitcoin
            n = float(sys.argv[1])
            # All the data of is converted in JSON and stored in price
            price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
            # the price of USD is stored under the "bpi" key, then the "USD" key, and finally the "rate_float" key.
            # You can access it like this:
            price_usd = price['bpi']['USD']['rate_float']

            #Conversion
            bitcoin_in_usd = n*price_usd

            #print price
            print(f'${bitcoin_in_usd:,.4f}')


        else:
            print('Command-line argument is not a number')
            sys.exit(1)
    else:
        print('Missing command-line argument')
        ys.exit(1)
except requests.RequestException:
    print("There was an error with the request.")
