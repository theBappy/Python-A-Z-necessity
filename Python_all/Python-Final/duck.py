# No race condition
file_name = 'text.txt'
try:
    f = open(file_name)
except IOError:
    print('no file exist')
else:
    with f:
        print(f.read())

# Race condition
# import os
# file_name = 'text.tx'
# if os.access(file_name, os.R_OK):
#     with open(file_name) as f:
#         print(f.read())
# else:
#     print("no such file accessed")


# Duck typing and easier to ask forgiveness than permission(EAFP)

# import os

# my_file = '/tmp/test.txt'

# Race condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print("File can not be accessed")


# No race condition
# try:
#     f = open(my_file)
# except IOError as e:
#     print('file can not be accessed')
# else: 
#     with f:
#         print(f.read())






# my_list =[1,2,3,4,5,6]

# if len(my_list) >= 6:
#     print(my_list[5])
# else:
#     print("that index does not exist")

# try:
#     print(my_list[5])
# except IndexError:
#     print('this index does not exist')



# person ={"name": "Jess", "age": 23, "Job": "Programmer"}
# # person = {
#     "name":"Jess", "age": 23
# }

# LBYL(Non-pythonic)
# if 'name' in person and 'age' in person and 'Job' in person:
#     print("I'm {name}. I', {age} years old and I'am a {Job}".formt(**person))
# else:
#     print("missing some keys")

# try:
#     print("I'm {name}, I'm {age} years old and I am a {Job}".format(**person))
# except KeyError as e:
#     print("missing {} key."format(e))



# class Duck:
#     def quack(self):
#         print('Quack, quack')
#     def fly(self):
#         print('flap, flap')
# class Person:
#     def quack(self):
#         print('i am quacking like a duck')
#     def fly(self):
#         print("i am  flappng my arms")

# def quack_and_fly(thing):
#     # Look before you leap(LBYL-non pythonic)

#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()
#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()

#     # thing.quack()
#     # thing.fly()
#     #  not duck typing(non-pythonic)
#     # if isinstance(thing, Duck):
#     #     thing.quack()
#     #     thing.fly()
#     # else:
#     #     print('this has to be a duck')
#     print()
        
# d = Duck()
# quack_and_fly(d)
# p = Person()
# quack_and_fly(p)   

