class Cars:
    #static variable/class vara=iable
    unit = 0
    def __init__(self, car, types, year):
        #instance variable
        self.car = car
        self.types = types
        self.year = year
        Cars.unit += 1
        print("Selling car with " + car)

car1 = Cars("Ford", "Mustang", 1974)   
print(Cars.unit)  #print out is 1   
car2 = Cars("Ferrari", "Roma", 2021)  
print(Cars.unit) # print out is 2
car3 = Cars("Mercedes", "C200", 1993)   
print(Cars.unit) # print out is 3