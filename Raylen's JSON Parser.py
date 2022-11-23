import requests
import json
import csv

fileName = "IA2.csv"
fields = []
rows = []

f = open(fileName, "r")
nameList = []
data = csv.reader(f)
for row in data:
        nameList.append(row[0])
print(nameList[1:10])

itemName = nameList[5]
space = " "
spaceURL = "%20"
itemInput = itemName.replace(space, spaceURL)
print(itemInput)
API_KEY = "63770fa41ddd970aef0e4ffe"
url = "https://backpack.tf/api/IGetPriceHistory/v1?item=" + itemInput + "&quality=Unique&tradable=Tradable&craftable=Craftable&priceindex=0&key=" + API_KEY

response = requests.get(url)

outData = json.dumps(response.json(), indent=4, sort_keys=True)
data = json.loads(outData)
print(outData)
with open("output.json", "w", encoding = "utf-8") as file:
        json.dump(response.json(), file, indent=4, sort_keys=True)
print(data["response"]["history"]["timestamp"])






