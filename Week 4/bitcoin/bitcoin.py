import json
import requests
import sys

if len(sys.argv) != 2:
   sys.exit("Missing command-line argument")

try:
   multiplier = float(sys.argv[1])
except ValueError:
   sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass

whole = response.json()
# print(json.dumps(whole, indent = 2))
# print(bitcoinJson["bpi"]["USD"]["code"])

bitcoin = whole["bpi"]["USD"]["rate_float"]
# bitcoin = float(bitcoin)
print(bitcoin)

price = bitcoin * multiplier

print(price)
print(f"${price:,.4f}")

# for result in whole["bpi"]["USD"]:
#    print(result)

# print(json.dumps(response.json(), indent = 2))
# print(whole["bpi"])