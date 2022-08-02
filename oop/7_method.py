# difference class method vs static method
# class method takes cls for first argument/parameter
# 

from datetime import date as dt

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # a class method to check age is adult or not
    @staticmethod
    def isAdult(age):
        if  age > 18:
            return True
        else:
            return False
    
    # a class method to create person object by year 
    @classmethod
    def birthdayYear(cls, name, year):
        return cls(name, dt.today().year - year)
    
        
#variable engineer use static method
engineer = Employee('Haerul', 17)
# variable hrd calls function class method 
hrd = Employee.birthdayYear('Farida', 1996)
print(engineer.age)
print(hrd.age)

print(Employee.isAdult(22))
print(Employee.isAdult(16))

