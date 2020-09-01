#!/bin/env python

import json

def save(fn, foodDict):
    with open("./data/"+fn+".json", 'w') as fp:
        json.dump(foodDict, fp)

data = open('data.txt').read()
print(data)
chunks = data.split('------')
for chunk in chunks:
    foodDict = {}
    lines = chunk.split('\n')
    for line in lines:
        if line != '':
            kvp = line.split((': '))
            print(bytes(kvp[0], 'utf-8'))
            print(bytes("Name", 'utf-8'))
            if kvp[0] == "Name":
                foodDict.update({"Name": kvp[1]})
            elif kvp[0] == "Visual":
                foodDict.update({"Visual": kvp[1]})
            elif kvp[0] == "Texture":
                foodDict.update({"Texture": kvp[1]})
            elif kvp[0] == "Smell":
                foodDict.update({"Smell": kvp[1]})
            elif kvp[0] == "Taste":
                foodDict.update({"Taste": kvp[1]})
            elif kvp[0] == "Main nutrient(s)":
                foodDict.update({"Main nutrient(s)": kvp[1].split(' - ')})
            elif kvp[0] == "Category":
                foodDict.update({"Category": kvp[1]})
        else:
            pass
    print(foodDict)
    save(foodDict["Name"], foodDict)