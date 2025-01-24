def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return  2 * x
    return inner
@decor1
@decor
def num():
    return 10

@decor
@decor1
def num2():
    return 10

print(num())
print(num2())




# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError("Radius cannot be negative")

#     @property
#     def area(self):
#         return 3.14159 * (self._radius ** 2)

# # Using the property
# c = Circle(5)
# print(c.radius) 
# print(c.area)    
# c.radius = 10
# print(c.area)


# class Employee:
#     raise_amount = 1.05

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
# Employee.set_raise_amount(1.10)
# print(Employee.raise_amount)

# class MathOperations:
#     @staticmethod
#     def add(x,y):
#         return x + y
# res = MathOperations.add(89,89)
# print(res)

# def fun(cls):
#     cls.class_name = cls.__name__
#     return cls
# @fun
# class Person:
#     pass
# print(Person.class_name)


# def method_decorator(func):
#     def wrapper(self, *args, **kwargs):
#         print('before calling the function')
#         res = func(self, *args, **kwargs)
#         print('after calling the function')
#         return res
#     return wrapper
# class MyClass:
#     @method_decorator
#     def say_hello(self):
#         print('Hello')
# obj = MyClass()
# obj.say_hello()



# def simple_decorator(func):
#     def wrapper():
#         print("before calling the function")
#         func()
#         print("after calling the function")
#     return wrapper

# @simple_decorator
# def greet():
#     print('hello world')
# greet()



# def greet(n):
#     return f'Hello , {n}'
# say_hi = greet
# say_hi
# print(say_hi('Alice'))

# def apply(f, v):
#     return f(v)
# res = apply(say_hi, 'Bob')
# print(res)

# def make_mult(f):
#     def mult(x):
#         return x * f
#     return mult
# dbl = make_mult(2)
# print(dbl(5))


# def fun(f, x):
#     return f(x)

# def square(x):
#     return x * x

# res = fun(square, 5)
# print(res)


# def decorator_name(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


# @decorator_name
# def function_to_decorate():
#     pass

# def decorator(func):

#     def wrapper():
#         print('Before calling the function')
#         func()
#         print("After calling the function")
#     return wrapper

# @decorator
# def greet():
#     print('Hello, world!')
# greet()

# def prefix_decorator(prefix):
#     def decorator_function(original_function):
#         def wrapper_function(*args, **kwargs):
#             print(prefix, "Executed before", original_function.__name__)
#             result = original_function(*args, **kwargs)
#             print(prefix, "Executed after", original_function.__name__, '\n')
#             return result
#         return wrapper_function
#     return decorator_function

# @prefix_decorator('LOG: ')
# def display_info(name, age):
#     print("display_info ran with argumetns({}, {})".format(name, age))

# display_info('John', 25)
# display_info('Travis', 30)