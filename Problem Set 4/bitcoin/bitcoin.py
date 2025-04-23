import sys
import requests
#importing library module

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        api_key = "YourApiKey"
        url = "https://rest.coincap.io/v3/assets/bitcoin"
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")
    except (KeyError, ValueError):
        sys.exit("Error parsing response data")

    total_cost = bitcoins * price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()