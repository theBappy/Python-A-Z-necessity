


# def decorator_funntion(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function

# @decorator_funntion
# def display():
#     print('display function run')

# @decorator_funntion
# def display_info(name,age):
#     print('display_info ran with arguments({}, {})'.format(name, age))

# display_info('John', 25)
# display()



# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function 
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)


# def outer_function(msg):
#     # message = msg
#     def inner_function():
#         print(msg)
#     return inner_function
# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')
# hi_func()
# bye_func()


# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result
# my_nums = square_numbers([1,2,3,4,5])


# class Duck:
#     def swim(self):
#         print('The duck is swimming')
#     def fly(self):
#         print('The duck is flying')
# class Swan:
#     def swim(self):
#         print("The swan is swimming")
#     def fly(self):
#         print('The swan is flying')
# class Albatross:
#     def swim(self):
#         print("The albatross is swimming")
#     def fly(self):
#         print('The albatross is flying')


# class Car:
#     def __init__(self, make,model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#     def start(self):
#         print('The car is starting')
#     def stop(self):
#         print('The car is stopping')
#     def drive(self):
#         print('The car is driving')
# class Truck:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#     def start(self):
#         print("The truck is starting")
#     def stop(self):
#         print('The truck is stopping')
#     def drive(self):
#         print('The truck is driving')


# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#     @abstractmethod
#     def start(self):
#         raise NotImplementedError("start() must ve implemented")
#     @abstractmethod
#     def stop(self):
#         raise NotImplementedError("stop() must be implemented")
#     @abstractmethod
#     def drive(self):
#         raise NotImplementedError("drive() must be implemented")
    