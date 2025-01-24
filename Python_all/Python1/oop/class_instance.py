# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com' 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
emp_1 = Employee('James', 'Anderson', 100000)
emp_2 = Employee('Rowan', 'Atkinson', 200000)

print(Employee.fullname(emp_1))
print(emp_2.fullname())

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Al-Amin'
# emp_1.last = 'Bappy'
# emp_1.email = 'abappy575@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'Corey'
# emp_2.last = 'Schafer'
# emp_2.email = 'corey.schafer@gmail.com'
# emp_2.pay = 600000

