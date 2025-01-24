class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)
    
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_work_day(my_date))

# emp_1_str = 'John-Doe-787878'
# emp_2_str = 'David-Beckham-9090990'
# emp_1_str = 'John-Doe-1787878'
# new_emp_1 = Employee.from_string(emp_1_str)

# print(new_emp_1.email)
# print(new_emp_1.fullname())


# fname, lname, pay = emp_1_str.split('-')
# new_emp_1 = Employee(fname, lname, pay)




# emp_1.set_raise_amount(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# print(Employee.num_of_emps)
# print(Employee.num_of_emps)


# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.email)
# print(emp_2.email)

# print(Employee.fullname(emp_1))
# print(emp_1.fullname())
# print(emp_2.fullname())


# print('{} {}'.format(emp_1.fname, emp_1.lname))

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Al-amin'
# emp_1.last = 'Bappy'
# emp_1.email = 'Al-amin.Bappy@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000