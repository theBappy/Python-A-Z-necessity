"""
LEGB -->
Local, Enclosing, Global, Build-in
"""

# x = 'global x'

# def test():
#     global x
#     x = 'local x'
#     # print(y)
#     print(x)
# x = 'global x'
# def test():
#     global x
#     x = 'local x'
#     print(x)
# test()
# print(x)

# import builtins
# print(dir(builtins))
# test()
# print(x)

# import builtins
# print(dir(builtins))
# def min():
#     pass

# m = min([8,7,65,9])
# print(m)

# def outer():
#     x ='outer x'
#     def inner():
#         x = 'inner x'
#         print(x)
#     inner()
#     print(x)
# outer()

# x = 'global x'

# def outer():
    # x ='outer x'
    # def inner():
        # nonlocal x
#         x ='inner x'
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

# def example():
#     x = 'legb rule'
#     print(x)
# example()
# print(x)

# def example_outer():
#     x ='outer function'
#     def example_inner():
#         y ='inner function'
#         print(f'{x}//{y}')
#     print(x)
#     example_inner()
# example_outer()

# str = 'global string'
# def example():
#     def example_inner():
#         print(str)
#     print(str)
#     example_inner()
# example()

# from math import pi

# def example_outer():
#     def example_inner():
#         print(pi)
#     print(pi)
#     example_inner()
# example_outer()
# x ='global scope'
# def example(x):
#     print(x)
# example('local scope')
# print(x)
# x = 'global scope'
# def example():
#     print(x)
# example()
# print(x)



