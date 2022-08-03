class Vehicle:
    def setVehicle(self, type):
        self.type = type

    def showVehicle(self):
        print(self.type)

class Manufacture:
    def setManufacture(self, country):
        self.country = country

    def showManufacture(self):
        print(self.country)


class Cars(Vehicle, Manufacture):

    def __init__(self, car, year):
        self.car = car
        self.year = year

Honda = Cars('Honda', 1993)
print('ini adalah object', Honda.__dict__)
Honda.setVehicle('City Car')
Honda.setManufacture('Japan')

Honda.showManufacture()
Honda.showVehicle()