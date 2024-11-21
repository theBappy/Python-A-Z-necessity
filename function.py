# def hello_func():
#     print('Hello function!')
# hello_func()
# def func(greeting, name='You'):
#     return '{}, {}'.format(greeting,name)
# print(func('Hi' , name = 'Corey'))


# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 34}

# student_info(*courses, **info)

# def my_function(*kids):
#     print('The youngest child is ' + kids[2])
# my_function('Emil', 'Tobias', 'Linus')

# months_days = [0,31,28,31,30,31,3031,31,30,31,30,31]

# def is_leap(year):
#     """Return True for leap years, False for non-leap years"""
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year,month):
#     """Return numvber of days in a month"""
#     if not 1 <= month <=12:
#         return 'Invalid month'
#     if month == 2 and is_leap(year):
#         return 29
#     return months_days[month]

# print(days_in_month(2024, 2))
# print(is_leap(2020))

# def my_function():
#     print('Hello form a function')
# my_function()

# def my_function(fname):
#     print(fname + 'Refsnes')
# my_function('Email ')
# my_function('Tobias ')
# my_function('Linus ')

# def my_function(fname,lname):
#     print(fname + " " + lname)
# my_function('John', 'Doe')

# def my_function(child3,child4,child5):
#     print('The youngest child is ' + child3)
# my_function(child3='Emil', child4='Linus', child5='Max')

# def my_function(**kid):
#     print('His last name is ' + kid['lname'])
# my_function(fname= 'tobias', lname= 'linus')

# def my_function(country = 'Norway'):
#     print('I am from ' + country)
# my_function('sweden')
# my_function()
# my_function('canada')
# my_function('south korea')

# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ['apple', 'cherry', 'mango']
# my_function(fruits)
# def my_function(x):
#     return 5 * x
# print(my_function(5))
# print(my_function(9))
# def my_function():
#     
# def my_function(x, /):
#     print(x)
# my_function(5)
# def my_function(x,/):
#     print(x)
# my_function(x=5)
# def my_function(*, x):
#     print(x)
# my_function(x = 8)
# def my_function(x):
#     print(x)
# my_function(4)
# def my_function(a,b, /, *, c, d):
#     print(a + b+ c+ d)
# my_function(5,6,c = 7,d = 8)
# def tri_recursions(k):
#     if(k>0):
#         result = k + tri_recursions(k-1)
#         print(result)
#     else: 
#         result = 0
#     return result
# print('Recursion example results: ')
# tri_recursions(10)
# if True:
#     pass
# if True:
#     print('Yes')
# if True: 
#     pass
# x = 10 
# y = 0 
# if (x > 0 and y) or (not y and x): 
#     print("Yes") 
# else: 
#     print("No")
# x, y, z = 0, -1, 1
# result = x or y and z
# print(result)
# x = [1, 2, 3]
# y = tuple(x)
# z = list(y)
# print(z == x)
# x = bool(5.5)
# print(x)
# if True: pass
# if True: print("Yes")
# if False: print("No") 
# else: print("Yes")
# if 0:  
#     print("Zero is True")  
# else:  
#     print("Zero is False")  