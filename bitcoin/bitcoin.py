import json
import requests
import sys

    # Check if there is at least one command-line argument
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        bitcoins_to_buy = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")



    bitcoin_data = response.json()

    usd_price = bitcoin_data["bpi"]["USD"]["rate"]
    usd_price = usd_price.replace(",", "")

    total_cost_usd = bitcoins_to_buy * float(usd_price)
    print(f"${total_cost_usd:,.4f}")