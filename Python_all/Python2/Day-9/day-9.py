# my_nums = (x*x for x in [1,2,3,4,5])
# print(list(my_nums))
# print(my_nums)
# for num in my_nums:
#     print(num)

# def square_numbers(nums):
#     for i in nums:
#         yield i * i
# my_nums = square_numbers([1,2,3,4,5])
# for num in my_nums:
#     print(num)


# print(my_nums)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result
# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums)

# from datetime import datetime
# birthday = datetime(1990,1,1)
# sentence = f'Jenn has a birthday on {birthday: %B %d, %Y}'
# print(sentence)

# pi = 3.141516
# sentence = f'Pi is eqaul to {pi:.4f}'
# print(sentence)

# for n in range(1,11):
#     sentence = f'The value is {n:02}'
#     print(sentence)

# calculation = f'4 times 11 is equal to {4 * 11}'
# print(calculation)

# first_name = 'Corey'
# last_name = 'Schafer'
# person ={'name':'John', 'age':23}
# sentence = f"My name is {person['name']} and I am {person['age']} years old"
# print(sentence)
# sentence = 'My name is {} and I am {} years in old'.format(person['name'], person['age'])
# print(sentence)

# sentence = f'My name is {first_name.upper()} {last_name.upper()}'
# print(sentence)

# sentence = 'My name is {} {}'.format(first_name, last_name)
# print(sentence)

# def divide(a,b, default=None):
#     if b == 0:
#         print('zero divisional detected')
#         return default
#     return a / b
# divide(8, 2)

# def to_integer(value):
#     try:
#         return int(value)
#     except ValueError:
#         return None
# to_integer('42')


# def to_integer(value):
#     if value.isdigit():
#         return int(value)
#     return None
# to_integer('two')


# from birds import Vehicle
# Vehicle('Ford', 'Mustang' , 'Red')


# from birds import Car, Truck
# vehicles = [
#     Car('Ford', 'Mustang', 'Red'),
#     Truck('Ford', 'F-150', 'Blue'),
# ]
# for vehicle in vehicles:
#     vehicle.start()
#     vehicle.drive()
#     vehicle.stop()

#try:
#     f= open('/Users/User/Desktop/Python (Phitron-FB)/Python2/testfile.txt')
    # if f.name == 'test_file.txt':
    #     raise Exception
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print('Error!')
# else:
#     print(f.read())
#     f.close()
# finally:
#     print('I am executing the finally')
# Pythonic
# Duck typing and easier to ask forgiveness than permission(EAFP)
# class Duck:
#     def quack(self):
#         print('Quack, Quack')
#     def fly(self):
#         print('Flap, Flap')
# class Person:
#     def quack(self):
#         print("I'm a Quacking like a duck!")
#     def fly(self):
#         print("I'm flapping my arms")
# def quack_and_fly(thing):
    # LBYL (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()
    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()
    # print()

    # EAFP(Pythonic)
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

#LBYL (Non-Pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print("I am {name}. I'm {age} in old and I am a {job}".format(**person))
# else:
#     print('Missing some keys')
# EAFP (Pythonic)
# person ={'name':'Jess', 'age':23}
# person = {'name':'Jess', 'age':23, 'job':'Prgrammer'}
# try:
#     print("I'm {name}, I am {age} years in old and I am a {job}".format(**person))
# except Exception as e:
#     print("Missing {} key.".format(e))
# if len(my_list) >= 6:
#     print(my_list[5])
# else:
#     print("That index does not exist")
# my_list = [1,2,3,4,5]
# try:
#     print(my_list[5])
# except IndexError:
#     print('That index does not exist')

# import os 
# myfile = '/Users/User/Desktop/Python (Phitron-FB)/Python2/testfile.txt'
#Race condition
# if os.access(myfile, os.R_OK):
#     with open(myfile) as f:
#         print(f.read())
# else:
#     print('File can not be accessed')

#No-Race condition
# try:
#     f = open(myfile)
# except IOError as e:
#     print('File does not exist')
# else:
#     with f:
#         print(f.read())
# class Specialstring:
#     def __len__(self):
#         return 21
# if __name__ == '__main__':
#     string = Specialstring()
#     print(len(string))
# class Bird: 
#     def fly(self): 
#         print("fly with wings") 
  
# class Airplane: 
#     def fly(self): 
#         print("fly with fuel") 
  
# class Fish: 
#     def swim(self): 
#         print("fish swim in sea") 

# for obj in Bird(), Airplane(), Fish(): 
#     obj.fly() 
# from birds import Duck, Swan , Albatross
# birds = [Duck(), Swan(), Albatross()]
# for bird in birds:
#     bird.fly()
#     bird.swim()
# numbers = [ 1,2,3]
# person = ('Jane', 24, 'Python Dev')
# letters = 'abc'
# ordinals = {'one':'first', 'two':'second', 'three':'third'}
# even_digits = {2,4,6,8}
# collections = [numbers, person, letters, ordinals, even_digits]

# for collection in collections:
#     for value in collection:
#         print(value)
# import csv
# import json
# from itertools import batched

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#     def read(self):
#         with open(self.filename) as file:
#             return[
#                 {
#                     "name": batch[0].strip(),
#                     "age": batch[1].strip(),
#                     "job": batch[2].strip(),
#                 }
#                 for batch in batched(file.readlines(),3)
#             ]
# class CSVReader:
#     def __init__(self, filename):
#         self.filename = filename
#     def read(self):
#         with open(self.filename, newline='') as file:
#             return list(csv.DictReader(file))
# class JSONReader:
#     def __init__(self, filename):
#         self.filename = filename
#     def read(self):
#         with open(self.filename) as file:
#             return json.load(file)
# readers = [
#     TextReader("/Python2/sample.txt"),
#     CSVReader("/Python2/sample.csv"),
#     JSONReader("/Python2/sample.json"),
# ]
# for reader in readers:
#     print(reader.read())