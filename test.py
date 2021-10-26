import json
from pprint import pprint

# Opening JSON file
try:
    file = open('data.json', encoding="utf8")
except Exception as e:
    print(e)
    # returns JSON object as
    # a dictionary
data = json.load(file)

# Iterating through the json
# list
sheet = 'SERVERS'

for key in data[sheet]:
    name = key["name"]
    for device in key["devices"]:
        print(name)
        pprint(device)
        print('\n')



# for key in data[sheet]:
#     print(key)
#     # print(key["name"])
#     print(key["devices"][0])
#     # print(key["devices"][0]['ip'])


# people = {"david": {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#
# print(people["david"]['name'])