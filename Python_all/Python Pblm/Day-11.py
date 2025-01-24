# print('Twinklw Twinke, litte star, \n\t How I wonder what you are! \n\t\tUp abode the world so high, \n\t\t Like a diamond in the sky. \n Twinkle, Twinkle , little star, \n\t\t How I wonder what you are!')
# import sys
# print("Python version")
# print(sys.version)
# print("Version info")
# print(sys.version_info)
# import sys
# print(sys.version)
# import datetime
# cdate = datetime.datetime.now()
# print(cdate)
# print("Current date and time:")
# print(cdate.strftime('%Y-%m-%d %H:%M:%S'))
# from math import pi
# print(pi * r *2)
# from math import pi 
# r = float(input("Input the radius of the circle: "))
# area = pi * r * 2
# print("The area of the circle is: " + str(r) +  str(area))
# fname = input("Enter your first name")
# lname = input("Enter your last name")
# print("Hello " + fname + lname)
# values = input("Input some comma-separated numbers: ")
# list = values.split(',')
# tuple = tuple(list)
# print('List: ' , list)
# print('Tuple: ' , tuple)
# filename = input('Enter your file name: ')
# f_extns = filename.split('.')
# print("The extensions of the file is: " + repr(f_extns[-1]))
# filename = input("Enter your file name here: ")
# f_extns = filename.split('.')
# print(f_extns)
# print("The extension of the file is: " + repr(f_extns[-1]))
# color_list = ['Red', 'Green', 'Blue']
# print(color_list[0], color_list[-1])
# exam_st_date = (11,12,2024)
# print("The examination will start from: %i/%i/%i" %exam_st_date)
# print("The examination will start on: %i/%i/%i" %exam_st_date)
# print("The examination will commence on: %i/%i/%i" %exam_st_date)
# a = int(input('Input an integer: '))
# n1 = int("%s" %a)
# n2 = int("%s%s" %(a, a))
# n3 = int("%s%s%s" %(a, a, a))
# n4 = int("%s%s%s%s" %(a, a, a, a))
# print(n1+n2+n3+n4)
# a = int(input("enter an integer number: "))
# n1 = int("%s" %a)
# n2= int("%s%s" %(a,a))
# n3= int("%s%s%s" %(a,a,a))
# n4= int("%s%s%s%s" %(a,a,a,a))
# n5= int("%s%s%s%s%s" %(a,a,a,a,a))
# print(n1+n2+n3+n4+n5)
# print(abs.__doc__)
# print(len.__doc__)
# print(sum.__doc__)
# print(map.__doc__)
# print(filter.__doc__)
# import calendar
# y = int(input('Input the year: '))
# x = int(input("Input the month: "))
# print(calendar.month(y, x))
# import calendar
# y = int(input("Input the year: "))
# x = int(input("Input the month: "))
# print(calendar.month(y,x))
# import calendar
# x = int(input("Input the year: "))
# y = int(input("Input the month: "))
# print(calendar.month(x,y))
# import calendar
# print(calendar.month(2024,12))
# import calendar
# print(calendar.month(22,12))
# print("""a string that you don't have to escape 
#       This is a ...... multi-line
#       heredoc string ------> example""")
# from datetime import date
# dt1 = date(2023,12,12)
# dt2 = date(2024,12,12)
# print((dt2-dt1).days)
# from math import pi
# r = 6
# v = 4/3 * pi * r**3
# print(v)
# def difference(n):
#     if n <= 17:
#         return 17 -n
#     else: 
#         return (n-17) * 2
# print(difference(12))
# print(difference(22))
# def near_difference(n):
#     return (abs(1000-n)<=100 or abs(2000-n)<=100)
# print(near_difference(1000))
# print(near_difference(900))
# print(near_difference(800))
# print(near_difference(2200))
# def sum_of_three_numbers(x,y,z):
#     sum = x + y + z
#     if x == y == z:
#         sum = sum * 3
#     return sum
# print(sum_of_three_numbers(1,2,3))
# print(sum_of_three_numbers(3,3,3))
# def new_string(text):
#     if len(text) >= 2 and text[:2]== "Is":
#         return text
#     else: 
#         return "Is" + text
# print(new_string('Array'))
# print(new_string('IsEmpty'))
# def larger_string(text, n):
#     result = ''
#     for i in range(n):
#          result = result + text
#     return result
# print(larger_string('abc', 2))
# print(larger_string('.py', 3))
# num = int(input('Enter a number: '))
# mod = num % 2
# if mod>0:
#     print("The number is odd.")
# else: 
#     print("The number is even.")
# def list_count(nums):
#     count = 0
#     for num in nums:
#         if num ==4: 
#             count += 1
#         return count
# def list_count(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count = count +1 
#     return count
# print(list_count([1, 4, 6, 7, 4]))
# def substring_copy(text , n):
#     flen = 2
#     if flen > len(text):
#         flen = len(text)
#     substr = text[:flen]
#     result = ''
#     for i in range(n):
#         result = result + substr
#     return result
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3))
# def is_vowel(str):
#     all_vowels ='aeiou'
#     return str in all_vowels
# print(is_vowel('c'))
# print(is_vowel('dog'))
# def group_member(data, n):
#     for value in data:
#         if n not in value:
#             return False
#         return True
# print(group_member([1, 5, 8, 3], 3))
# print(group_member([5, 8, 3], -1))
# def histogram(items):
#     for n in items:
#         output =''
#         times = n
#         while times > 0:
#             output += '*'
#             times -= 1
#         print(output)
# histogram([2,3,4,5])
# def histogram(items):
#     for n in items:
#         output =''
#         times = n
#         while times > 0:
#             output += '*'
#             times -=1
#         print(output)
# histogram([1,2,3,4,5,6,7,8,9])
# def concatenate_str(lst):
#     result =''
#     for element in lst:
#         result += str(element)
#     return result
# print(concatenate_str([1,5,12,4]))
# def concatenate_str(lst):
#     result  =''
#     for n in lst:
#         result += str(n)
#     return result
# print(concatenate_str([12,13,14,5]))
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
# ]
# for x in numbers:
#     if x == 237:
#         print(x)
#         break
#     elif x % 2 ==0 :
#         print(x)
# for x in numbers:
#     if x == 237:
#         print(x)
#         break
#     elif x % 2 == 0 :
#         print(x)
    # for  x in numbers:
#     if x == 237:
#         print(x)
#         break
#     elif x % 2 == 0:
#         print(x)
# color_list_1= set(['white', 'black', 'red'])
# color_list_1 = set(['red', 'green'])
# print(color_list_1.intersection(color_list_1))
# b = int(input('Input the base: '))
# c = int(input('Input the height: '))
# area = b * c/2
# print(area)
# def gcd(x,y):
#     gcd = 1
#     if x % y ==0:
#         return y
#     for k in range(int(y/2), 0 , -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#     return gcd
# print(gcd(12,17))
# print(gcd(4,6))
# print(gcd(336,360))
# def gcd(x,y):
#     z = x % y
#     while z:
#         x = y
#         y = z
#         z = x % y
#     return y
# from functools import reduce
# from math import gcd as _gcd
# def gcd(nums):
#     return reduce(_gcd, nums)
# print(gcd([336,360]))
# print(gcd([12,17]))
# print(gcd([4,6]))
# print(gcd([2,30,36]))
# def lcm(x,y):
#     if x>y:
#         z = x
#     else:
#         z = y
#     while True:
#         if(z % x ==0) and (z %y==0):
#             lcm = z
#             break
#         z += 1
#     return lcm
# print(lcm(4,6))
# print(lcm(15,17))
# from functools import reduce
# from math import gcd
# def lcm(numbers):
#     return reduce((lambda x, y : int(x*y/gcd(x,y))), numbers)
# print(lcm([12,7]))
# print(lcm([1,3,4,5]))
# print(lcm([4,6]))
# print(lcm([15,17]))
# def sum_of_three(x,y,z):
#     if x== y or y ==z or z==x:
#         sum = 0
#     else: 
#         sum = x+ y+z
#     return sum
# print(sum_of_three(2,1,2))
# print(sum_of_three(8,8,8))
# def test_number(x,y):
#     if x == y or abs(x-y)== 5 or (x+y)==5:
#         return True
#     return False
# print(test_number(7, 2))
# print(test_number(3, 2))
# print(test_number(2, 2))
# print(test_number(7, 3))
# print(test_number(27, 53))
# def add_numbers(a,c):
#     if not (isinstance(a,int) and isinstance(c,int)):
#         return a + c
# def add_numbers(x,y):
#     if not (isinstance(x,int) and isinstance(y, int)):
#         return x + y
# def add_number(x,y):
#     if not (isinstance(x,int) and isinstance(y, int)):
#         return x + y
# def add_numbers(x,y):
#     if not (isinstance(x,int) and isinstance(y, int)):
#         return x + y
# print(add_numbers(10,20))
# print(add_numbers(10,20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))
# def personal_details():
#     name, age = 'Simon', 19
#     address = 'Bangalor, Karnataka, India'
#     print("Name:{}\nAge:{}\nAddress:{}".format(name, age, address))
# personal_details()
# x, y = 4,3
# result = x * x + 2 *x *y+y*y
# print("({}+{})^2={}".format(x,y,result))
# amt = 10000
# int = 3.5
# years = 7
# future_value = amt * ((1 + (0.01 * int))*years)
# print(round(future_value)*2)        
# import math
# p1 = [4,0]
# p2 = [6,6]
# distance = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))
# print(distance)
# import math
# p1 = [4,0]
# p2 = [6,6]
# distance = math.sqrt(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))
# distance = math.sqrt(((p1[0]-p1[0])**2+(p1[1]-p2[1])**2))
# print(distance)
# import os.path
# print(os.path.isfile('main.txt'))
# print(os.path.isfile('Day-10.py'))
# import struct
# print(struct.calcsize('P')*8)
# import struct
# print(struct.calcsize("P")*8)
# import struct
# print(struct.calcsize("P")*8)
# import struct
# print(struct.calcsize("P")*8)
# import struct
# print(struct.calcsize("P")*8)
# import struct
# print(struct.calcsize("P")*8)
# import struct
# print(struct.calcsize("P")*8)
# import struct
# print(struct.calcsize("P")*8)
# import platform
# import struct
# arhcitecture = platform.architecture()[0]
# print(arhcitecture)
# import platform
# architecture = platform.architecture()[0]
# print(architecture)
# import platform
# x = platform.architecture()[0]
# print(x)
# import struct
# print(struct.calcsize("P")*8)
# import platform
# n = platform.architecture()[0]
# print(n)
# import platform
# import os
# print(os.name)
# print(platform.__name__)
# print(platform.system())
# print(platform.release())
# import os
# import platform
# print(os.name)
# print(platform.system())
# print(platform.release())
# print(os.name)
# print(platform.release())
# print(platform.system())
# print(os.name)
# print(platform.release())
# print(platform.system())
# import os
# import platform
# print(os.name)
# print(platform.release())
# print(platform.system())
# import os
# import sys
# import platform
# import sysconfig
# print(os.name)
# print(platform.release())
# print(platform.system())
# print(sysconfig.get_platform())
# print(platform.machine())
# print(platform.architecture())
# import site
# print(site.getsitepackages())
# import site
# print(site.getsitepackages())
# import site
# print(site.getsitepackages())
# import site
# print(site.getsitepackages())
# import site
# print(site.getsitepackages())
# import site
# print(site.getsitepackages())
# from subprocess import call
# print(call['is', '-i'])
# import os
# print(os.system('ls -l'))
# import psutil
# print(psutil.cpu_count())
# import os
# print(os.path.realpath(__file__))
# import os 
# print(os.path.)relpath(__file__)
# import os
# print(os.path.realpath(__file__))
# import os
# print(os.path.realpath(__file__))
# import os 
# print(os.path.realpath(__file__))
# import os 
# print(os.path.realpath(__file__))
# import os
# print(os.path.realpath(__file__))
# import os
# print(os.path.realpath(__file__))
# import multiprocessing
# cpu_count = multiprocessing.cpu_count()
# print(cpu_count)
# import multiprocessing
# print(multiprocessing.cpu_count())
# import multiprocessing
# print(multiprocessing.current_process)
# import multiprocessing
# print(multiprocessing.cpu_count())
# import multiprocessing
# print(multiprocessing.cpu_count())
# import multiprocessing
# print(multiprocessing.cpu_count())
# import multiprocessing
# print(multiprocessing.cpu_count())
# import multiprocessing
# print(multiprocessing.cpu_count())
# import _multiprocessing
# print(multiprocessing.cpu_count())
# n = '5656.766'
# print(float(n))
# print(int(float(n)))
# print(int(n))
# print(float(n))
# n = "246.2458"
# a = float(n)
# print(a)
# print(int(a))
# def test(s):
#     try:
#         return int(s)
#     except ValueError:
#         return float(s)
# def test(s):
#     try:
#         return int(s)
#     except ValueError:
#         return float(s)
# def test(s):
#     try:
#         return int(s)
#     except ValueError:
#         return float(s)
# def test(s):
#     try:
#         return int(s)
#     except ValueError:
#         return float(s)
# print(test('12'))
# print(test('233.44455'))
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# print(files_list)
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# print(files_list)
# for i in range(1,10):
#     print('*', end='')
# print('\n')
# for i in range(1,10):
#     print(i)
#     print('*', end='')
# print('\n')
# import functools
# printf = functools.partial(print, end='')
# for i in range(1,10):
#     printf('*')



