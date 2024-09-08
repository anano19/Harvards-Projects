import json
import requests
import sys


try:
    bitcoin = float(sys.argv[1])
except IndexError:
    sys.exit("Error: Argument must be a number.")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
except requests.RequestException:
    sys.exit("Error")


number = bitcoin * response['bpi']['USD']['rate_float']
print(f"${number:,.4f}")
