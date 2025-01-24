'''
LEGB
Local, Enclosing, Global, Built-in
'''
# x = 'global x'
# def test():
#     # global x
#     x = 'local x'
#     # print(y)
#     print(x)
# test()
# print(x)
# def test(z):
#     x = 'local x'
#     print(z)
# test('local z')
# print(z)
# import builtins
# print(dir(builtins))
# def my_min():
#     pass
# m = min([5,1,4,2,3])
# print(m)
# import builtins
# print(dir(builtins))
# import builtins
# print(dir(builtins))
# import builtins
# print(dir(builtins))
# import builtins
# print(dir(builtins))
# import builtins 
# print(dir(builtins))
# x ='global x'
# def outer():
#     x = 'outer x'
#     def inner():
#         x = 'inner x'
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)
# my_list = [0,1,2,3,4,5,6,7,8,9]
# print(my_list[::-3])
# print(my_list[::-2])
# print(my_list[::-1])
# print(my_list[::-1])
# print(my_list[-2:1:-2])
# print(my_list[-2:1:-1])
# print(my_list[2:-1:-1])
# print(my_list[2:-1:3])
# print(my_list[0:6:3])
# print(my_list[2:-1:2])
# print(my_list[:])
# print(my_list[:])
# print(my_list[:])
# print(my_list[5:])
# print(my_list[:-2])
# print(my_list[1:])
# print(my_list[1:])
# print(my_list[1:-2])
# print(my_list[-7:-2])
# print(my_list[3:8])
# print(my_list[0:6])
# list[start:end:step]
# print(my_list[-10])
# sample_url = 'http://coreyms.com'
# print(sample_url[::-1])
# print(sample_url[-4:])
# print(sample_url[7:])
# print(sample_url[7:-4])
# nums = [1,2,3,4,5,6,7,8,9,10]
# mylist =[(letter, num) for letter in 'abcd' for num in range(4)]
# print(mylist)
# mylist =[(x, y) for x in 'abc' for y in range(5)]
# print(mylist)
# mylist =[(letter,num) for letter in 'abcd' for num in range(5)]
# print(mylist)
# mylist = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(mylist)
# mylist =[]
# for letter in 'abcd':
#     for num in range(4):
#         mylist.append((letter, num))
# print(mylist)
# mylist =[]
# for letter in 'abcd':
#     for num in range(4):
#         mylist.append((letter, num))
# print(mylist)
# mylist =[]
# for leter in 'abcd':
#     for num in range(4):
#         mylist.append((leter, num))
# print(mylist)
# mylist = filter(lambda n: n %2 ==0, nums)
# print(mylist)
# mylist = [n for n in nums if n %2 ==1]
# print(mylist)
# mylist = [n for n in nums if n % 2 ==0]
# print(mylist)
# mylist = []
# for n in nums:
#     if n %2 ==0:
#         mylist.append(n)
# print(mylist)
# mylist = map(lambda n: n*n, nums)
# print(mylist)
# mylist = [n*n for n in nums]
# print(mylist)
# mylist =[n*n for n in nums]
# print(mylist)
# mylist = []
# for n in nums:
#     mylist.append(n*n)
# print(mylist)
# my_list = [n for n in nums]
# print(my_list)
# my_list =[]
# for n in nums:
#     my_list.append(n)
# print(my_list)
# nums = [1,2,3,4,5,6,7,8,9,10]
# mydict = {name:hero for name, hero in zip(names, heroes)}
# print(mydict)
# mydict ={name:hero for name, hero in zip(names,heroes)}
# mydict={name:hero for name, hero in zip(names,heroes)}
# mydit ={name:hero for name,hero in zip(names,heroes)}
# mydict ={name:hero for name,hero in zip(names,heroes)}
# mydict = {name: hero for name, hero in zip(names,heroes)}
# print(mydict)
# mydict = {name: hero for name, hero in zip(names, heroes)}
# print(mydict)
# mydict ={}
# for name,hero in zip(names,heroes):
#     mydict[name] = hero
# print(mydict)
# mydict ={}
# for name, hero in zip(names,heroes):
#     mydict[name] =hero
# print(mydict)
# mydict ={}
# for name, heor in zip(names,heroes):
#     mydict[name]=heroes
# print(mydict)
# mydict ={}
# for name, hero in zip(names,heroes):
#     mydict[name] = hero
# print(mydict)
# x=zip(names, heroes)
# print(x)
# mydict ={name:hero for name,hero in zip(names,heroes) if name != 'Peter'}
# print(mydict)
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = [ 'Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# myset = set()
# for n in nums:
#     myset.add(n)
# print(myset)
# myset = set()
# for n in nums:
#     myset.add(n)
# print(myset)
# myset =set()
# for n in nums:
#     myset.add(n)
# print(myset)
# nums = [1,2,3,1,3,4,5,5,6,7,7,8,7,9,9]
# myset1 = {n for n in nums}
# print(myset1)
# print(type(myset1))
# def gen_func(nums):
#     for n in nums:
#         yield n*n
# my_gen= gen_func(nums)
# my_gen=[]
# for i in my_gen:
#     print i
# def gen_func(nums):
#     for n in nums:
#         yield n * n
# my_gen = gen_func(nums)
# for i in my_gen:
#     print(i)
# def gen_func(nums):
#     for n in nums:
#         yield n * n
# my_gen = gen_func(nums)
# for i in my_gen:
#     print(i)
# def gen_func(nums):
#     for n in nums:
#         yield n * n
# my_gen = gen_func(nums)
# for i in my_gen:
#     print(i)
# def gen_func(nums):
#     for n in nums:
#         yield n * n
# my_gen = gen_func(nums)
# for i in my_gen:
#     print(i)
# my_gen =(n*n for n in nums)
# for i in my_gen:
#     print(i)
# my_gen = (n*n for n in nums)
# for i in nums:
#     print(i)
# my_gen = (n*n for n in nums)
# for i in nums:
#     print(i)
# nums =[1,2,3,4,5,6,7,8,9,10]
# my_gen = (n*n for n in nums)
# for i in my_gen:
#     print(i)
# li = [9,1,8,2,7,3,6,4,5]
# s_li = li.sort()
# s_li = sorted(li, reverse=True)
# print('Sorted variable:\t', s_li) # New sorted list
# li.sort(reverse=True)
# print('Original variable:\t', li)
# tup = (9,1,8,2,7,3,6,4,5)
# s_tup = sorted(tup)
# print('Tuple\t', s_tup)
# di ={'name':'corey', 'age':34, 'id':'coreyid'}
# s_di = sorted(di)
# print('Dict\t', s_di)
# print(s_li)
# s_li = sorted(li,key=abs)
# print(s_li)
# s_li = sorted(li, key=abs)
# s_li = sorted(li, key=abs)
# print(s_li)
# s_li = sorted(li, key=abs)
# print(s_li)
# li =[-6,-5,-4,2,1,3]
# s_li = sorted(li, key=abs)
# print(s_li)
# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def __repr__(self):
#         return '({},{},{})'.format(self.name, self.age, self.salary)
# from operator import attrgetter
# e1 = Employee('Carl', 37, 70000)
# e2 = Employee('Sarah', 29, 80000)
# e3 = Employee('John', 43, 90000)
# employees =[e1,e2,e3]
# def e_sort(emp):
#     return emp.salary
# s_emloyees = sorted(employees, key=attrgetter('age'))
# print(s_emloyees)
# sentence ='My name is {} and I am {} years old'.format(person['name'], person['age'])
# print(sentence)
# sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
# print(sentence)
# tag ='h1'
# text = 'This is a headline'
# sentence = '<{0}>{1}</{0}>'.format(tag,text)
# print(sentence)
# person = {"name": "John", "age":23}
# l = ['John', 23]
# sentence = 'My name is {0[0]} and I  am {0[1]} years old'.format(l)
# print(sentence)
# class Person():
#     def __init__(self, name, age):
#         self.name= name
#         self.age = age
# p1 = Person('Jack', '33')
# sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
# print(sentence)
# sentence = 'My name is {name} and I am {age} years old'.format(name='John', age='30')
# print(sentence)
# person ={'name':'Jenn', 'age':23}
# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)
# for i in range(1,11):
#     sentence = 'The value is {:02}'.format(i)
#     print(sentence)
# for i in range(1,11):
#     sentence = 'The value is {:02}'.format(i)
#     print(sentence)
# for i in range(1,11):
#     sentence = "The value is {:03}".format(i)
#     print(sentence)
# pi = 3.14151617
# sentence = 'Pi is equal to {:.3f}'.format(pi)
# print(sentence)
# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)
# import datetime
# my_date = datetime.datetime(2016,9,24,12,30,45)
# print(my_date)
# sentence = '{:%B %d , %Y}'.format(my_date)
# print(sentence)
# import datetime
# my_date = datetime.datetime(2023,12,2,12,14,40)
# sentence = '{:%B %d, %Y}'.format(my_date)
# sentence = '{"%B %d, %y}'.format(my_date)
# print(sentence)
# sentence = '{:%B %d, %Y}'.format(my_date)
# print(sentence)
# import datetime
# mydate = datetime.datetime(2024,12,6,12,12,12)
# sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(mydate)
# print(sentence)