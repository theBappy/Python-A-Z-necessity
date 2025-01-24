# for i in range(10):
#     print(i)
# nums =[1,2,3,4,5]
# for num in nums:
#     for letter in 'abc':
#         if num == 3:
#             print('Found!')
#             continue
#         print(num, letter)
# for num in nums: 
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)
# for i in range(1,11):
#     print(i)
# x = 0
# while x < 10:
#     print(x)
#     x += 1
# x = 0 
# while x < 10:
#     if x == 5:
#         print('Found!')
#         continue
#     print(x)
#     x += 1
# x = 0 
# while True:
#     if x == 5:
#         break
#     print(x)
#     x += 1
# def hello_func():
#     pass
# print(hello_func())
# def hello_func():
#     print('Hello Function!')
# hello_func()
# def hello_func():
#     print('Hello Function!')
# print('Hello Function')
# print('Hello Function')
# print('Hello Function')
# print('Hello Function')
# print('Hello Function')
# def hello_func():
#     print('Hello Function')
# hello_func()
# hello_func()
# hello_func()
# hello_func()
# DRY = Don't Repeat Yourself
# def hello_func():
#     return 'Hello World'
# print(hello_func().upper())
# print(hello_func().lower())
# print(hello_func().capitalize())
# print(len('Test'))
# def hello_func(greeting , name='John'):
#     return '{}, {} Function'.format(greeting, name)
# print(hello_func('Hi', name='Davis'))
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 25}
# student_info(*courses, **info)
# month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# def is_leap(year):
#     '''Return true for leap years, and false for non-leap year'''

#     return  year %4 == 0 and (year % 100 !=0 or year % 400 ==0)

# def days_in_month(year, month):
#     if not 1 <= month <=12:
#         return 'Invalid month'
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month]
# print(is_leap(2017))
# print(is_leap(2020))
# print(days_in_month(2017,2))
# print(days_in_month(2020,2))
# print(days_in_month(2020,12))
# print('Imported my module...')
# test = 'Test String'
# def find_index(to_search, target):
#     # Find the index of a value in sequence
#     for i , value in enumerate(to_search):
#         if value == target:
#             return i
#     return -1
# import antigravity
# import antigravity
# import os 
# print(os.__file__)
# print(os.__file__)
# print(os.getcwd())
# print(os.getcwd())
# print(os.getcwd())
# print(os.getcwd())
# print(os.getcwd())
# print(os.getcwd())
# print(os.getcwd())
# print(os.getcwd())
# import os
# print(os.getcwd())
# import datetime
# import calendar
# print(calendar.isleap(2020))
# print(calendar.isleap(2019))
# print(calendar.isleap(2024))
# print(calendar.isleap(3015))
# print(calendar.isleap(2017))
# td = datetime.date.today()
# print(td)
# today = datetime.date.today()
# today = datetime.date,today()
# todat = datetime.date.today()
# today = datetime.date.today()
# today = datetime.date.today()
# print(today)
# today = datetime.date.today()
# print(today)
# import math
# rads = math.radians(270)
# print(rads)
# print(math.sin(rads))
# import math
# rads = math.radians(90)
# print(rads)
# print(math.sin(rads))
# import math
# rads = math.radians(145)
# print(rads)
# import math
# courses=['Art', 'Englisg', 'CompSci', 'Math']
# rads = math.radians(90)
# print(math.sin(rads))
# random_course = random.choice(courses)
# random_course = random.choice(courses)
# random_course = random.choice(courses)
# random_course = random.choice(courses)
# random_course = random.choice(courses)
# print(random_course)
# import random 
# courses = ['History', 'Math', 'Physics', 'CompSci']
# random_course = random.choice(courses)
# print(random_course)
# import day_4 as mm
# from day_4 import find_index
# from day_4 import find_index , test
# from day_4 import find_index as fi, test
# from day_4 import find_index, test
# from day_4 import *
# import sys
# sys.path.append('/Python1/test.txt')
# from day_4 import find_index , test
# courses = ['History', 'Math', 'Physics', 'CompSci']
# index = find_index(courses, 'Math')
# print(index)
# print(test)
# print(sys.path)
# cars[2]= 'Mercedes'
# print(cars[0])
# print(cars[1])
# print(cars[2])
# print(len(cars))
# for x in cars:
#     print(x)
# cars =['Volvo' , 'Ford', 'BMW']
# cars.append('Mercedes')
# print(cars)
# cars.pop(1)
# print(cars)
# cars.pop()
# print(cars)
# cars.reverse()
# print(cars)
# class MyClass: 
#     x = 5
# p1 = MyClass()
# print(p1.x)
# class Person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
# p1 = Person('John', 24)
# print(p1.age)
# print(p1.name)
# class Person:
#     def __init__(self, name , age):
#         self.age = age
#         self.name = name
#     def myfunc(self):
#         print('hello my name is ' + self.name)

# p1 = Person('John', 36)
# p1.age = 56
# p1.myfunc()
# print(p1.age)
# del p1.age
# print(p1)
# class Person:
#     pass
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, firstname, lastname, year):
#         super().__init__(firstname, lastname)
#         self.graduationyear = year
#     def welcome(self):
#         print("welcome", self.firstname, self.lastname, "to the class of " , self.graduationyear)

        
# x = Person('John', 'Doe')
# x.printname()
# x = Student('Mike', 'Tysen', 2019)
# print(x.graduationyear)
# x.welcome()
# mytuple = ('apple', 'banana', 'cherry')
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# mystr = 'banana'
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# mytuple = ('apple', 'banana', 'cherry')
# for x in mytuple:
#     print(x)
# mystr = 'apple'
# for x in mystr:
#     print(x)
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x 
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# myclass = MyNumbers()
# myiter = iter(myclass)
# for x in myiter:
#     print(x)
# x = 'Hello World'
# print(len(x))
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print('Drive')
# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print('Sail')
# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Fly")
# car1 = Car('Ford', 'Mustang')
# boat1 = Boat('Ibiza',  'Touring 20')
# plane1 = Plane('Boeing', '747')
# for x in (car1, boat1, plane1):
#     x.move()
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Move")
# class Car(Vehicle):
#     pass
# class Boat(Vehicle):
#     def move(self):
#         print("Sail")
# class Plane(Vehicle):
#     def move(self):
#         print('Fly')
# car1= Vehicle('Ford', 'Mustang')
# boat1 = Vehicle('Ibiza', 'Touring 78')
# plane1= Vehicle('Boeing', '747')
# for x in (car1, boat1, plane1):
#     print(x.brand)