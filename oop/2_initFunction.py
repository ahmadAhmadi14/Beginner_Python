# initialize function connects with attribute. always there argument self in initfunction
class Car:
    def __init__(self, car, types, year, color):
        #instance variable
        self.car = car
        self.types = types
        self.year = year
        self.carColor = color


car1 = Car("Ford", "Mustang", 1974, "red")
print(car1.__dict__) # print out object of car1
print(car1.types) # print out attribute types of car1 --> Mustang