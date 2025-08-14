import requests
import sys
import json

def main():
    coins = get_coin_number()
    get_price(coins)

def get_coin_number():
    if len(sys.argv) == 2:
        try:
            if float(sys.argv[1]):
                return sys.argv[1]
        except ValueError:
            print("Invalid value for command-line argument")
    else:
        print("Invalid number of command-line arguments")
        sys.exit(1)

def get_price(coin_no):
    api_request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    temp_object= api_request.json()
    usd = temp_object["bpi"]["USD"]["rate_float"]
    result = float(usd) * float(coin_no)
    print(f"${result:,.4f}")

if __name__ == "__main__":
    main()
