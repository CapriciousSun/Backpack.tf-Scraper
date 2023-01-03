import requests
import json
import csv

import CSVReader

fileName = "IA2.csv"
fields = []
rows = []

f = open(fileName, "r")

data = csv.reader(f)
for row in data:
        CSVReader.nameList.append(row[0])
print(CSVReader.nameList[1:10])

space = " "
spaceURL = "%20"
apostrophe = "'"
apostropheURL = "%27"

for i in CSVReader.nameList:
        itemName = i
        itemInput = itemName.replace(space, spaceURL)
        finalInput = itemInput.replace(apostrophe, apostropheURL)
        API_KEY = "63770fa41ddd970aef0e4ffe"
        url = "https://backpack.tf/api/IGetPriceHistory/v1?item=" + itemInput + "&quality=Unique&tradable=Tradable&craftable=Craftable&priceindex=0&key=" + API_KEY

        response = requests.get(url)

        outData = json.dumps(response.json(), indent=4, sort_keys=True)
        data = json.loads(outData)

        with open("output.json", "w", encoding = "utf-8") as file:
                json.dump(response.json(), file, indent=4, sort_keys=True)
        print(i + ": " + str(data["response"]["history"][len(data["response"]["history"]) - 1]["value"]))

y = open(fileName, "w")

f.close();