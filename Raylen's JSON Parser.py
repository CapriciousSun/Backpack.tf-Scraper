import requests
import json
import csv

nameList = []
testList = ["Bonk Boy", "Trucker's Topper", "Flair!"]
tempList = []
finalList = []

with open("IA2 working copy.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    for line in csv_reader:
            nameList.append(line[0])

fileName = "IA2.csv"
fields = []
rows = []

f = open(fileName, "r")

space = " "
spaceURL = "%20"
apostrophe = "'"
apostropheURL = "%27"
exclamation = "!"
exclamationURL = "%21"

for i in nameList:
        itemName = i
        removeSpace = itemName.replace(space, spaceURL)
        removeApostrophe = removeSpace.replace(apostrophe, apostropheURL)
        finalInput = removeApostrophe.replace(exclamation, exclamationURL)
        API_KEY = "63770fa41ddd970aef0e4ffe"
        url = "https://backpack.tf/api/IGetPriceHistory/v1?item=" + finalInput + "&quality=Unique&tradable=Tradable&craftable=Craftable&priceindex=0&key=" + API_KEY

        response = requests.get(url)

        outData = json.dumps(response.json(), indent=4, sort_keys=True)
        data = json.loads(outData)

        with open("output.json", "w", encoding = "utf-8") as file:
                json.dump(response.json(), file, indent=4, sort_keys=True)
        print(i + ": " + str(data["response"]["history"][len(data["response"]["history"]) - 1]["value"]))
        tempList = [i, str(data["response"]["history"][len(data["response"]["history"]) - 1]["value"])]
        finalList.append(tempList)

print(finalList)

testList = [["Bonk Boy", 1.77], ["Trucker's Topper", 3.44], ["Flair!", 3.11]]

with open("IA2.csv", "w") as new_file:
    csv_writer = csv.writer(new_file)

    csv_writer.writerows(finalList)

f.close();