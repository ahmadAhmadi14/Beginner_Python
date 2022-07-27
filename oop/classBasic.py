class Car: # Template
    pass

car1 = Car() # object
car2 = Car()
car3 = Car()

car1.name = "Ford" # name = Ford is attribute
car1.type = "Mustang" #  type = mustang is attribute
car1.year = 1974 # year = 1974 is attribute

car2.name = "Ferrari" 
car2.type = "Roma"
car2.year = 2021

car3.name = "Mercedes" 
car3.type = "C200" 
car3.year = 1993

print(car1) #is car1 object? true or false (true, because)
print(car1.__dict__)