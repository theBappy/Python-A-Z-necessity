# Duck typing and Easier to Ask Forgiveness than Permission (EAFP)
# Pythonic(clear and readble code writing technique)

# import os
# my_file ='data.txt'

# Race condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print('File cannot be accessed')

# No Race-condition
# try:
#     f = open(my_file)
# except IOError as e:
#     print('File can not be accessed')
# else:
#     with f:
#         print(f.read())
#         f.close()


# my_list =[1,2,3,4,5,6]

# Pythonic
# try:
#     print(my_list[5])
# except IndexError:
#     print('The index does not exist')

# Non-pythonic
# if len(my_list) >= 6:
#     print(my_list[5])
# else:
#     print('This index does not exist')


# person ={"name":"john", "age": 23, "job": "programmer"}
# person = {"name":"john", "age": 23}


# LBYL(Non-pythonic/Asking Permission)
# if 'name' in person and 'age' in person and 'job' in person:
#     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# else:
#     print('Missing some keys')

# EAFP (Pythonic)
# try:
#     print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# except KeyError as e:
#     print('Missing {} key.'.format(e))



# class Duck: 
#     def quack(self):
#         print('Quack, quack')
#     def fly(self):
#         print('Flap, Flap')

# class Person:
#     def quack(self):
#         print('I am quacking like a duck')
#     def fly(self):
#         print('I am flapping my arms')


# def quack_and_fly(thing):
#     # Not duck-typed(Non-pythonic)
#     if isinstance(thing, Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print('This has to be a duck')
    
#     print()



# def quack_and_fly(thing):
#     thing.quack()
#     thing.fly()
#     print()



# def quack_and_fly(thing):
    # LBYL (Non-pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()


# def quack_and_fly(thing):
#     # EAFP (Pythonic)
#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)

#     print()


# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)
