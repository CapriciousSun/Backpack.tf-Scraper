import requests
import json
import operator

itemName = "Exquisite Rack"
itemInput = ""
space = operator.indexOf(itemName, " ")
itemInput = itemName[0:space] + "%20" +itemName[space + 1:len(itemName)]
print(itemInput)
API_KEY = "63770fa41ddd970aef0e4ffe"
url = "https://backpack.tf/api/IGetPriceHistory/v1?item=" + itemInput + "&quality=Unique&tradable=Tradable&craftable=Craftable&priceindex=0&key=" + API_KEY

response = requests.get(url)

outData = json.dumps(response.json(), indent=4, sort_keys=True)
data = json.loads(outData)
print(outData)
with open("output.json", "w", encoding = "utf-8") as file:
        json.dump(response.json(), file, indent=4, sort_keys=True)
print(data["response"]["history"][100]["timestamp"])
