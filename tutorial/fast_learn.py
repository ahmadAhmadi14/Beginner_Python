from operator import truediv


fruits = ["apple","banana", "cherry", "kiwi", "manggo"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


buah = ["apel", "pisang", "kiwi", "jeruk", "mangga"]
lisBaru = [x for x in fruits if "a" in x]

print(lisBaru)

buah1 = ["apple", "manggo", "cherry", "banana", "kiwi"]
buah1.sort()
print(buah1)

number = [100, 78, 36, 52, 10, 45]
number.sort()
print(number)

#descending
buah2 = ["apple", "manggo", "cherry", "banana", "kiwi"]
buah2.sort(reverse = True)
print(buah2)

#descending
number1 = [100, 78, 36, 52, 10, 45]
number1.sort(reverse= True)
print(number1)

# if else
a = 5
b = 6
if a % 5 and b % 6:
    print("KAS")