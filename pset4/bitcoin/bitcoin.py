import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    while True:
        try:
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            break
        except requests.RequestException:
            pass
    request = r.json()
    price = float(request['bpi']['USD']['rate_float'])
    total = amount * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()