# sample inheritance for employee
# employee has division accounting, human resource and sales

class Employee:

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

class AccountingEmployee(Employee):
    pass

class HumanResource(Employee):
    pass

class Sales(Employee):
    pass


employee1 = Employee('Agus', 23, 'admin')
finance = AccountingEmployee('Lina', 20, 'Staff accounting')
hrd = HumanResource('Samuel', 36, 'Head HRD')
sales1 = Sales('Rio', 40, 'sales software')
print(f' this is name {employee1.name} for class')
print(f'sub class has employee position is {finance.position}')
print(hrd.age)
print(sales1.position)