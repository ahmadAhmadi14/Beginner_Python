# things about encapsulation
# all variable are private
# to consume data uses getter & setter methods
class Car:
    def __init__(self, car, types, year):
        # private member
        self.car = car
        # private members to restrict access
        # avoid direct data modification
        self.__types = types
        self.__year = year

    def show(self):
        print(f'Car Details:, {self.car}, {self.__types}, with year: {self.__year}')

    # getter methods
    def get_year(self):
        return self.__year

    # setter method to modify data member
    # condition to allow data modification with rules
    def set_year(self, number):
        if number > 50:
            print('Car must changes')
        else:
            self.__year = number

sedan = Car('Toyota', 'Camry', 1993)

# before Modify
sedan.show()
# changing roll number using setter
sedan.set_year(60)


sedan.set_year(25)
sedan.show()
