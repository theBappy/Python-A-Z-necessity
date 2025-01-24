# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def helo():
#     return "Hello World"

# @app.route('/about')
# def about():
#     return 'About Page'

# if __name__ == "__main__":
#     app.run()
# def prefix_decorator(prefix):
#     def decorator_function(original_function):
#         def wrapper_function(*args, **kwargs):
#             print(prefix, 'Executed Before', original_function.__name__)
#             result = original_function(*args, **kwargs)
#             print(prefix, 'Executed After', original_function.__name__, '\n')
#             return result
#         return wrapper_function
#     return decorator_function

# @prefix_decorator('TESTING:')
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('John', 25)
# display_info('Travis', 30)

# from collections import namedtuple
# color = (55,155,255)
# color1 = {'red': 55, 'green': 155, 'blue': 255}
# print(color[0])
# print(color1['red'])
# from collections import namedtuple
# Color = namedtuple('Color', ['red', 'green', 'blue'])
# color = Color(55,155,25)
# white = Color(255,255,255)
# print(color[0])
# print(color.red)
# print(color.green)
# print(color.blue)
# print(white.blue)
# from collections import namedtuple
# Color = namedtuple('Color', ['red', 'green', 'blue'])
# color = Color(55,155,255)
# white=Color(255,245,235)
# print(color.blue)
# print(color.red)
# print(white.blue)
# print(white.red)

# Python Object Oriented Programming

# print(emp_2.fullname())
# print(Employee.fullname(emp_1))

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())
# print('{} {}'.format(emp_1.first,emp_1.last))

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 50000

# print(emp_1.email)
# print(emp_2.email)


# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
    
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last , pay = emp_str.split('-')
#         return cls(first, last, pay)
    
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True


# emp_1 = Employee('Corey', 'Scahfer', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# import datetime
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))



# emp_1_str = 'John-Doe-70000'
# emp_2_str = 'Steve-Smith-300000'
# emp_3_str = 'Jane-David-90900'

# new_emp_1 = Employee.from_string(emp_1_str)
# print(new_emp_1.email)
# print(new_emp_1.fullname())
# print(new_emp_1.pay)


# first, last , pay = emp_1_str.split('-')
# new_emp_1 = Employee(first, last, pay)
# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)



# print(Employee.num_of_emps)

# emp_1.raise_amount= 1.06
# print(emp_1.__dict__)

# print(Employee.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# class Employee:
    
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'


#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# class Developer(Employee):
#     raise_amount = 1.10

#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
    
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
    
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
    
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->' , emp.fullname())
              

# dev_1 = Developer('Corey', 'Scahfer', 50000 , 'Python')
# dev_2 = Developer('Test', 'User', 60000, 'Java')

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(isinstance(mgr_1 ,Manager))
# print(isinstance(mgr_1 , Employee))
# print(isinstance(mgr_1, Developer))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
# print(issubclass(Manager , Developer))
# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()


# print(dev_1.email)
# print(dev_1.prog_lang)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)

# class Employee:
    
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

#     def __repr__(self):
#         return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(), self.email)
    
#     def __add__(self, other):
#         return self.pay + other.pay
    
#     def __len__(self):
#         return len(self.fullname())

# dev_1 = Employee('Corey', 'Scahfer', 50000 )
# dev_2 = Employee('Test', 'User', 60000)


# print(len(dev_1))
# print(len(dev_2))

# print('test'.__len__())

# print(len('Test'))

# print(dev_1+ dev_2)


# print(dev_1.__repr__())
# print(dev_1.__str__())

# print(repr(dev_1))
# print(str(dev_1))

# print(dev_1)
# print(1 + 2)
# print(int.__add__(5 , 8))
# print(str.__add__('a', 'b'))

class Employee:
    

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
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
        
    
emp_1 = Employee('John', 'Smith')

# emp_1.first = 'Jim'
emp_1.fullname = 'David Warner'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

