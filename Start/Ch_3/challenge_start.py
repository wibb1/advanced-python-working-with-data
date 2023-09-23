# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

from audioop import reverse
import datetime
import json
import csv
import pprint


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

quakes = data['features']
# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def get_sig(dataitem):
    significance = dataitem["properties"]["sig"]
    if (significance is None):
        significance = 0
    return float(significance)

def get_date(dataitem):
    return dataitem["properties"]["time"]

quakes.sort(key=get_sig, reverse=True)
sig_quakes = quakes[:40]

sig_quakes.sort(key=get_date, reverse=True)

header = ['Magnitude', 'Place', 'Felt Reports', 'Date', 'Coordinates']
rows=[]

for quake in sig_quakes:
    q = quake['properties']
    formatted_date = datetime.date.fromtimestamp(int(q['time']/1000))
    formatted_url = f"https://maps.google.com/maps/search/?api=1&query={quake['geometry']['coordinates'][1]}%2C{quake['geometry']['coordinates'][0]}"
    rows.append([q['mag'], q['place'], q['felt'], formatted_date, formatted_url])

with open("challenge.csv" , "w", newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
