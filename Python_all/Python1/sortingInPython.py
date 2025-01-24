# li =[9,8,1,2,7,4,5,6]

# tup =(9,8,1,2,7,4,5,6)
# s_tup = sorted(tup)
# print('Tuble\t',s_tup )

# di ={'name': 'logan', 'job':'superhero', 'age': None, 'os': 'Mac'}

# s_di = sorted(di)
# print('Dict\t', s_di)

# s_li = sorted(li,reverse=True)
# print('Sorted Varibale:\t', s_li)
# li.sort(reverse=True)
# print('Original Varibale:\t', li)

# s_li = sorted(li)
# print('Sorted Variable:\t',s_li)
# li.sort()
# print('Original Variable:\t', li)

# li = [-6,-5,-4,2,1,3]
# s_li=sorted(li, key=abs)
# print(s_li)
# s_li = sorted(li, key=abs)
# print(s_li)
# s_li = sorted(li, key=abs)
# print(s_li)

# class Employee():
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age= age
#         self.salary = salary
#     def __repr__(self):
#         return'({},{},{})'.format(self.name, self.age, self.salary)
# from operator import attrgetter

# e1 = Employee('John', 34, 34543)
# e2= Employee('Sarah', 33, 56746)
# e3 =Employee('Stark', 36, 57346)

# employees =[e1,e2,e3]
# # def e_sort(emp):
# #     return emp.salary

# s_employees = sorted(employees, key=attrgetter('age'), reverse=True)
# print(s_employees)