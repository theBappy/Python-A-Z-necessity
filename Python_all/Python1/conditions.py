x = 2
print(x==2)
print(x==3)
print(x>2)
print(x<4)
name ='john'
age = 23
if name == 'john' and age == 23:
    print('Your name is John who is 23 years in old!')
if name == 'john' or name =='ricky':
    print('Your name is either jogn or ricky')
name = 'john'
if name in ['john','ricky']:
    print('Your name is john')
age = 34
if age in [34,43,55,23]:
    print('Your age is between 30 to 35')
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass
statement = True
another_statement = False
if statement is True: 
    pass
elif another_statement is True: 
    pass
else:
    pass
statement = True
another_statement = False
if statement is True:
    pass
elif statement is False:
    pass
else:
    pass
x = 7
if x == 5:
    print('the value of x is 5')
else: 
    print('the value of x is not 5')
x = [1,2,3]
y = [1,2,3]
print(x==y)
print(x is y)
print(not True)
print(not False)
print((not False)==(False))
print((not True)==(False))
number = 10
second_number =10
first_array = [1,2,3]
second_array = [1,2]
if number > 15:
    print('1')
if first_array:
    print('2')
if len(second_array)==2:
    print('3')
if len(first_array)+len(second_array)==5:
    print('4')
if first_array and first_array[0]==1:
    print('5')
if not second_array:
    print('6')
