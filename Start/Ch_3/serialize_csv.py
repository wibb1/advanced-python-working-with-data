# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))

# TODO: Create the header and row structures for the data
header = ["Place", "Magnitude","Date","Link"]
rows = []
# TODO: populate the rows with the resulting quake data
for quake in largequakes:
    q = quake['properties']
    formatted_date = datetime.date.fromtimestamp(int(q['time']/1000))
    rows.append([q['place'], q['mag'], formatted_date, q['url']])
    
# TODO: write the results to the CSV file
with open("largequakes.csv" , "w", newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
    