class Cars:
    #static variable/class variable
    unit = 0
    def __init__(self, car, types, year):
        #instance variable
        self.car = car
        self.types = types
        self.year = year
        Cars.unit += 1

    # void function, method without argumen and return
    def name(self):
        print("The incridible car is " + self.car) # alllow with car1.name() . print out incridible ford

    # method with argumen
    def secondProduction(self, wheel):
        self.year += wheel

    # method with argumen and return
    def getSecondProduction(self):
        return self.year

car1 = Cars("Ford", "Mustang", 1974)   
car2 = Cars("Ferrari", "Roma", 2021)

car1.name()
car1.secondProduction(4)

print(car1.getSecondProduction())
