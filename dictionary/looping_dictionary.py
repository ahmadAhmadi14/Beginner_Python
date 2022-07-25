# looping dictionary

thisDict = {
    "car": "Ford",
    "model": "Mustang",
    "year": 1974
}

for x in thisDict:
  print(x) # just key

#operator to get item/iterables
keys = thisDict.keys()
print(keys) # print keys

values = thisDict.values()
print(values)

items = thisDict.items()
print(items) # print key and values

for keys, values in thisDict.items():
    print(f'{keys} = {values}')
