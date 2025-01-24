def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(7)


# def myfunction(n):
#     return lambda a : a *n
# mydoubler = myfunction(2)
# mytripler = myfunction(3)

# print(mydoubler(6))
# print(mytripler(6))


# def myfunction(n):
#     return lambda a : a * n
# mytripler = myfunction(3)
# print(mytripler(7))

# def myfunction(n):
#     return lambda a : a * n
# mydoubler = myfunction(2)
# print(mydoubler(7))

# def myfunction(n):
#     return lambda a : a *n 

# x = lambda a, b, c : a + b + c
# print(x(1,2,3))

# x = lambda a, b : a * b
# print(x(5,6))

# x = lambda a : a + 20
# print(x(5))

# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
# tri_recursion(5)

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
# print("Recursion example results: ")
# tri_recursion(7)


# def myfunction(a, b, / , *, c, d):
#     print(a*b*c*d)
# myfunction(2,3, c= 4, d= 5)


# def myfunction(a,b, / , *,c,d):
#     print(a+b+c+d)
# myfunction(5,6,c=7,d=9)

# def myfunction(*, x):
#     print(x)
# myfunction(x=9)

# def myfunction(*, a):
#     print(a)
# myfunction(a=898989)

# def myfunction(*,  x):
#     print(x)
# myfunction(x=9)

# def myfunction(x , /):
#     print(x)
# myfunction(x=5)

# def myfunction(a, /):
#     print(a)
# myfunction(88)


# def myfunction(a, /):
#     print(a)
# myfunction(9)

# def myfunction(y, /):
#     print(y)
# myfunction(6)

# def myfunction(x , /):
#     print(x)
# myfunction(4)

# def myfunction():
#     pass

# def myfunction(x):
#      return 5 * x
# print(myfunction(4))
# print(myfunction(7))
# print(myfunction(9))

# def myfunction(food):
#     for x in food:
#         print(x)
# fruits = ['apple','banana','cherry']
# myfunction(fruits)

# def myfunction(country='Sweden'):
#     print("I am from " + country)
# myfunction('USA')


# def myfunction(**kwargs):
#     print('My name is ' + kwargs['lname'])
# myfunction(fname='John', lname='Doe')

# def myfunction(child3, child2, child1):
#     print("The youngest son is: " + child3)
# myfunction(child1="Emil", child2="John", child3="David")

# def myfunction(*kids):
#     print("The youngest son is " + kids[2])
# myfunction('John', 'Doe', 'David')

# def myfunction(*args):
#     print("The youngest child is " + args[2])
# myfunction("Emil", "Tobias", "John")

# def myfunction(fname, lname):
#     print(fname + " " + lname)
# myfunction("John", "Doe")


# def myfunction(fname):
#     print(fname + "Refsnes")
# myfunction("Email ")
# myfunction("John ")
# myfunction('David ')


# def my_function():
#     print("This is a function!")
# my_function()


# for x in [1,2,3]:
#     pass


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)


# for x in range(6):
#     if x == 3: 
#         break
#     print(x)
# else:
#     print("Finally Finised!")

# for x in range(6):
#     print(x)
# else:
#     print("Finally finished")

# for x in range(5, 50, 5):
#     print(x)


# for x in range(5, 11, 2):
#     print(x)

# for x in range(10):
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == 'banana':
#         continue
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     if x == 'banana':
#         break
#     print(x)

# fruits = ['apple', 'cherry', 'banana']
# for x in fruits:
#     print(x)
# for z in "test":
#     print(z)


# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print('i is no longer less than 6')

# i = 1
# while i < 6:
#     i += 1
#     if i == 3: 
#         print("Found!")
#         break 
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# x = 11
# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also abode 20!")
#     else: 
#         print("but not above 20")

# a = 33
# b = 200
# if not a > b:
#     print("a is NOT greater than b")

# a = 200
# b = 33
# c = 500
# if a > b or a >c:
#     print("At least one condition is true")

# print("A") if a > b else print("=") if a == b else print("B")

# print("A") if a > b else print("B")
# if a > b: print("a is greater than b")
# if b > a:
#     print("b is greater than a")
# else:
#     print("a is greater than b")

# a = 200
# b = 33
# if b > a:
#     print('b is greater than a')
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def is_leap(year):
#     """Return True for leap years, False for non-leap years.(This  is called aDoc-String)"""

#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# def days_in_month(year, month):
#     """Return number of days in that month in that year."""

#     if not 1 <= month <= 12:
#         return 'Invalid Month'

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]

# print(is_leap(2020))
# print(days_in_month(2020, 2))


# def hello_func(greeting, name='John'):
#     return "{}, {}".format(greeting, name)

# print(hello_func('Hey',name='David'))
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22, 'married': False}

# student_info(*courses, **info)

# print(hello_func().upper())

# print(len('Test'))

# DRY (Don't repeat yourself)

# print("Hello World.")
# print("Hello World.")
# print("Hello World.")
# print("Hello World.")

# x  = 0

# while True:
#     if x == 5:
#         break       
#     print(x)
#     x += 1

# for i in range(1, 11):
#     print(i)

# nums =[1, 2, 3, 4, 5]

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)



# condition = 'Test'
# if condition:
#     print('Evaluate to True')
# else:
#     print('Evaluate to False')

# a = [1,2,3]
# b = [1,2,3]
# print(id(a))
# print(id(b))
# print(a is b)
# print(id(a) == id(b))

# user = 'Admin'
# logged_in = True

# if not logged_in:
#     print("Please Log In")
# else: 
#     print("Welcome")


# language = 'Java'
# if language == 'Python':
#     print('Language is python')
# elif language == 'Java':
#     print("Language is Java")
# elif language == 'JavaScript':
#     print("Language is JavaScript")
# else:
#     print('No match')