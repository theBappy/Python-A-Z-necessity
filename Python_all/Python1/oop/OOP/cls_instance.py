#  Python Object-Oriented Programming

class Employee:    
   
    raise_amount = 1.04

    def __init__(self, first , last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Al-Amin','Bappy',50000, 'Python')
emp_2 = Employee('Test','User',60000, 'Java')

print(emp_1)


# print(1+2)
# print('a'+'b')

# class Employee:    
   
#     raise_amount = 1.04

#     def __init__(self, first , last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@gmail.com'
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# class Developer(Employee):
#     raise_amount = 1.10

#     def __init__(self, first , last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self, first, last, pay , employees= None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees =  employees
    
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())
     

# dev_1 = Developer('Al-Amin','Bappy',50000, 'Python')
# dev_2 = Developer('Test','User',60000, 'Java')

# mgr = Manager('Sue', 'Smith', 90000, [dev_1])

# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Developer))

# print(isinstance(mgr, Manager))
# print(isinstance(Manager, Employee))
# print(isinstance(mgr, Developer))


# print(mgr.email)

# mgr.add_emp(dev_2)
# mgr.remove_emp(dev_1)

# mgr.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first , last, pay)

#     @staticmethod
#     def is_work_day(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True



# import datetime
# my_date = datetime.date(2016,7,10)
# print(Employee.is_work_day(my_date))


# emp_1_str = 'John-Doe-70000'
# emp_2_str = 'Steve-Smith-80000'
# emp_3_str = 'Jane-Doe-90000'


# new_emp_1 = Employee.from_string(emp_1_str)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# first, last , pay = emp_1_str.split('-')
# new_emp_1 = Employee(first, last, pay)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# first, last , pay = emp_1_str.split('-')
# new_emp_1 = Employee(emp_1_str)
# print(new_emp_1.email)
# print(new_emp_1.pay)


# emp_1.set_raise_amount(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.num_of_emps)
# print(Employee.num_of_emps)

# emp_1.raise_amount =1.06

# print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(Employee.__dict__)

# print(emp_1.__dict__)
# print(emp_2.did)

# print(emp_1.__dict__)
# print(emp_2.__dict__)

# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)


# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount
# Employee.raise_amount


# print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())


# emp_1.first = 'Al-Amin'
# emp_1.last = 'Bappy'
# emp_1.email = 'Alamin.Bappy@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@gmail.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)
