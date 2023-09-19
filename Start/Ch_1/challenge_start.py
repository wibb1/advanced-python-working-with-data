# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def filter_felt(q):
    if q['properties']['felt'] is None or q['properties']['felt'] <= 100:
        return False
    else:
        return True

def get_felt(quake):
    felt=quake['properties']['felt']
    if felt is None:
        return float(0)
    else:
        return float(felt)
    
def get_sig(quake):
    sig = quake['properties']['sig']
    if sig is None:
        return 0
    else:
        return sig

quakes = data['features']
felt_by_100_list = list(filter(filter_felt, quakes))
felt_by_100_list.sort(key=get_felt, reverse=True)

print(f"1. Total quakes: {len(quakes)}")
print(f"2. Quakes Felt by >= 100 people: {len(felt_by_100_list)}")
print(f"3. most felt by = {felt_by_100_list[0]['properties']['place']} reports: {felt_by_100_list[0]['properties']['felt']}")


def get_sig(dataitem):
    significance = dataitem["properties"]["sig"]
    if (significance is None):
        significance = 0
    return float(significance)

def transform_sig(quake):
    q = quake['properties']
    return {
        "magnitude": q['mag'],
        "place": q['place'],
        "significance": q['sig']
    }

quakes.sort(key=get_sig, reverse=True)
sig_list = quakes
print('4. Most significant events \n')
for i in range(0,10):
    print(f"Event: Magnitude: {sig_list[i]['properties']['mag']} \nLocation: {sig_list[i]['properties']['place']} \nSignificance: {sig_list[i]['properties']['sig']}")
