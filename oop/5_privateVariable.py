class Cars:
    # class variable
    unit = 0
    __privateUnit = 0 #cannot accessed

    def __init__(self,name,types,year):
        self.name = name
        self.types = types
        self.year = year
        #variable instance private
        self.__private = "private"
        #variable instance protedted
        self._protected = "protected"

car1 = Cars("Toyota","Camry",2019)

print(car1.__dict__)
print(Cars.__dict__)
print(car1._protected)