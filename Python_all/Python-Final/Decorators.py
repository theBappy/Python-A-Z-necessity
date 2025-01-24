# Decorators

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function()


# hi_func = outer_function('hi')
# bye_func = outer_function('bye')

# def decorator_function(originial_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed  this before {}'.format(originial_function.__name__))
#         return originial_function(*args, **kwargs)
#     return wrapper_function

# # class decorator_class(object):
# #     def __init__(self, original_function):
# #         self.original_function = original_function
# #     def __call__(self, *args, **kwargs):
# #         print('call method executed  before {}'.format(self.originial_function.__name__))
# #         return self.originial_function(*args, **kwargs)

# @decorator_function
# def display():
#     print('display function ran')


# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))
# display_info('John', 25)

# display()

