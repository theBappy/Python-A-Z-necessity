class Employee:

   
    raise_amt = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname + '.' + lname + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.pay)

    def __str__(self):
        return '{} -  {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay  + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(len(emp_1))
# print(len(emp_2))

# print(len('Test'))

# print('test'.__len__())

# print(emp_1 + emp_2)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1 + 2)
# print(int.__add__(5,6))
# print(str.__add__('a', 'b'))






