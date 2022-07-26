'''intro args and kwargs'''

def function_car(car, type, year):
    print(f"this {car} with type of {type} is so special because this car released {year}")
function_car('Ford', 'Mustang', 1974)

# writing with *args
def function_car(*data):
    car = data[0]
    types = data[1]
    year = data[2]
    print(f"this is {car} yoooo with type {types} and {year} for release year.")
function_car("Ford", "Mustang", 1974)

# addition function with args
def addition(*number):
    data = 0
    for x in number:
        data = data + x
    print(data)
addition(5,6,7)    

# writing with **kwargs, There is key in dictionary
def function_kwargs(**kwargs):
    # print(kwargs) result -> dictionary {name = "Ford", Type = "Mustang", Year = 1974}
    name = kwargs["name"]
    types = kwargs["types"]
    year = kwargs["year"]
    print(f"Wow, this is {name} {types} and released {year}")

function_kwargs(name = "Ford", types = "Mustang", year = 1974)
