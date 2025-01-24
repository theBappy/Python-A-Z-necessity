# try:
#     print(x)
# except:
#     print('An exception occurred')
# try:
#     print(x)
# except NameError:
#     print('Variable x is not defined')
# except:
#     print('Somethins else went wrong')
# try:
#     print('Hello')
# except:
#     print('something went wrong')
# else:
#     print('nothing went wrong')
# try:
#     print(x)
# except:
#     print('something went wrong')
# finally:
#     print('the try except is finished')
# try: 
#     f = open('demofile.txt')
#     try:
#         f.write('lorum ipsum')
#     except:
#         print('something went wrong')
#     finally:
#         f.close()
# except:
#     print('something went wrong opening the file')
# x = -1
# if x < 0:
#     raise Exception('Sorry, no numbers below zero')
# x = 'hello'
# if not type(x) is int:
#     raise TypeError('only integers are allowed')