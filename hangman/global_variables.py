x = "awesome"

def myFunc():
    x = "fantastic"
    print("Python is " + x)
myFunc()

print("Python is " + x)

b = "Hello world"
print(b[:5])

c = "Hello world"
print(c[6:])

quantity = 3
itemsno = 7
price = 49.49
myOrder = "I wan {0} pieces dollars to {2} pieces of item {1}"
print(myOrder.format(quantity, price, itemsno))