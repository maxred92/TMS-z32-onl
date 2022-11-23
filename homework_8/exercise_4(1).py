import json
import random 


def f(name,age):
    names = dict(zip(name, age))
    dictonary = {}
    for x, y in names.items():
        dictonary[random.randint(100000, 999999)] = {'name': x, 'age': y}
    with open('test.json',mode ='w') as file:
        json_file = json.dump(dictonary, file, indent=4)
name = 'Tim', 'John', 'Sally', 'Trevor', 'Harry'
age = (12,34,24,57,16)