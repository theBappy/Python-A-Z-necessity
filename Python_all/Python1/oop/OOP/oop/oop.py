#  Python Object-Oriented Programming

class Employee:    
   
    raise_amount = 1.04

    def __init__(self, first , last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}@email.com'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('John', 'Doe')

emp_1.fullname ='Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

# class Employee:    
   
#     raise_amount = 1.04

#     def __init__(self, first , last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@gmail.com'
#         self.pay = pay
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

#     def __repr__(self):
#         return "Employee('{}', '{}' ,{})".format(self.first, self.last, self.pay)
    
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(), self.email)

#     def __add__(self, other):
#         return self.pay + other.pay
    
#     def __len__(self):
#         return len(self.fullname())
    

# emp_1 = Employee('Al-Amin','Bappy',50000)
# emp_2 = Employee('Test','User',60000)

# print(len(emp_1))
# print(len(emp_2))

# print(len('test'))
# print('testa'.__len__())

# print(emp_1 + emp_2)

# print(emp_1)
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1+2)
# print(int.__add__(3,4))
# print(str.__add__('a', 'b'))