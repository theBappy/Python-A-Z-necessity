class Employee:
    def __init__(self,name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

from  operator import attrgetter

e1 = Employee('Card', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees =[e1,e2,e3]

# def e_sort(emp):
#     return emp.salary

# s_employees = sorted(employees, key=lambda e: e.salary)
# s_employees = sorted(employees, key=attrgetter('age'))
s_emp = sorted(employees, key=attrgetter('age'), reverse=True)
print(s_emp)

# li = [-6,-5,-4,1,2,3]
# s_li = sorted(li, key = abs)
# print(s_li)


# tup = (9,1,8,2,3,7,6,4,5)
# di ={'name:':'John', 'job':'Progamming', 'age': None, 'os':'Mac'}
# s_di = sorted(di)
# print(s_di)


# s_tup = sorted(tup, reverse=True)
# print(s_tup)


# li = [9,1,8,2,3,7,6,4,5]

# s_li = sorted(li, reverse=True)
# print("Sorted Variable:\t", s_li)

# li.sort(reverse=True)
# print("Original Variable:\t", li)


# s_li = sorted(li)
# print(s_li)

# s_li = sorted(li)
# print(s_li)
# print(li(sorted))

# s_li =sorted(li)
# print(s_li)