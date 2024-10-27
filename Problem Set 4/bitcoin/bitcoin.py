import sys 
import requests

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin_price = response["bpi"]["USD"][rate_float]
    total_amount = bitcoin_price * value 
    print(f"{total_amount:,.4f}")
execept requests.RequestException:
    print("Website Not Resonding. Please Try Later")

cek 123
