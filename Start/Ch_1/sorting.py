# Example file for Advanced Python: Working With Data by Joe Marini
# sorting data with the sorted() and sort() functions

import json


# numbers = [42, 54, 19, 17, 23, 31, 16, 4]
# names = ["Jeff", "Bill", "Addie", "Stephanie", "Zach", "Lukas", "Joe", "Stacy"]
# print("start")
# print(numbers)
# print(names)
# # TODO: the sorted() function can be used to return a new list with sorted data
# new_numbers = sorted(numbers)
# new_names = sorted(names)
# print("sorted")
# print(new_numbers)
# print(new_names)
# # TODO: alternately, you can use the list object's sort() method, which sorts the list in-place
# print("reversed")
# new_numbers.sort(reverse=True)
# new_names.sort(reverse=True)

# print(new_numbers)
# print(new_names)
# # TODO: To sort custom objects, we can tell the sort function which property to use
# # by specifying a key function

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def get_mag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

data['features'].sort(key=get_mag, reverse=True)
for i in range (0, 10):
    print(data['features'][i]['properties']['place'])