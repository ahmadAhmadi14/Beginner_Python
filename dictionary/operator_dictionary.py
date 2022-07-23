# operator dictionary

thisDict = {
    "car": "Ford",
    "type": "Mustang",
    "year": 1974
}

LENDICT = len(thisDict)
print(f'panjang thisDict adalah {LENDICT}')

#check key exist or not
KEY = "car"
CHECKKEY = KEY in thisDict
print(f'are there {KEY} in {CHECKKEY}') #if exist is True

#access value (read) with get
print(thisDict["car"])
# print(thisDict.get("lamp"))
print(thisDict.get("lamp", "is not found"))

# update data
thisDict["color"]= "red"
print(f"update {thisDict} with red color")

#delete data
del thisDict["year"]
print(f"this is delete year car from data {thisDict}")