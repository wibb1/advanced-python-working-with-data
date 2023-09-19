# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict
from pprint import PrettyPrinter

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# use the event type to classify and count the number of occurrences of each in the following format
# earthquake      : 11558
# explosion       : 85
# quarry blast    : 81
# ice quake       : 17
# other event     : 4

quakeCounter = defaultdict(int)

for quake in data['features']:
    quakeCounter[quake['properties']['type']] += 1
    
for type in quakeCounter:
    tab = '\t'
    print(f"{type}{tab}: {quakeCounter[type]}")
