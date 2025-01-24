quantity = 3
itemno = 456
price = 59

txt = "the price is {:.3f}".format(price)
print(txt)

# txt = "I want {} pieces of item number {} for {:.2f} dollars".format(quantity, itemno, price)
# print(txt)




# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
# print(myorder.format(quantity, itemno, price))


# myorder = " i have a {carname} , it is a {model}"
# print(myorder.format(carname='ford', model='mustang'))

# age = 45
# name = 'john'
# txt = "his name is {1}. {1} is {0} years old".format(age,name)
# print(txt)

# price = 50000
# txt = f"the price is {price:-} dollars"
# print(txt)

# def myfunc(x):
#     return x * 0.345
# txt = f"the plane is flying at a{myfunc(67000)} meter altitude"
# print(txt)

# fruits = "apples"
# txt = f"i love {fruits.upper()}"
# print(txt)

# price = 90
# txt = f"it is very {'Expensive' if price>50 else 'cheap'}"
# print(txt)


# price = 89
# tax = 0.25
# txt = f"the price is { price + (price * tax)} dollars"
# print(txt)

# price = 78
# txt = f"the price is {89 * 10:.2f} dollars"
# print(txt)

# txt = f"The price is 57 dollars"
# print(txt)


# username = input('Enter username')
# print('Username is ' + username)

# x = 'hello'
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")


# x = -1
# if x < 0:
#     raise Exception("sorry, no numbers below zero")

# try:
#     f = open("demo.txt")
#     try:
#         f.write('Lorum ipsum')
#     except:
#         print("something went wrong")
#     finally:
#         f.close()
# except:
#     print("something went wrong")


# try:
#     print(x)
# except:
#     print("something went wrong")
# finally:
#     print("the 'try except' is finished")

# try:
#     print("hello")
# except:
#     print("something went wrong")
# else:
#     print("nothing went wrong")


# try:
#     print(x)
# except NameError:
#     print("Variable is not defined")
# except:
#     prin("Something else went wrond")

# try:
#     print(x)
# except:
#     print("An exception occurred")