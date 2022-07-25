# list array
data_list = [5, 7, 4, 16]
print(data_list)
print(data_list[0])

# with {} -> set. 
data_set = {5, 2, 90, 51, 87}
print(data_set) # ascending
# print(data_set[0]) --> error 'set' object is not subscriptable

#tuples
tuples = (6, 7, 18, 10, 3)
print(tuples)
print(tuples[0])

# tuples[0] = 57 --> TypeError: tuple object does not support in item assignment

# dictionary (dict) -> associate array
# identifier = key

thisDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

print(thisDict['brand'])