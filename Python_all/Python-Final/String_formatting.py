import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)

sentence = '{0:%B %d %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(my_date)
print(my_date)

# sentence = '{0:%b %d %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
# print(sentence)


# print(my_date)

# mydate = '{:%b %d %Y}'.format(my_date)
# print(mydate)

# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)


# pi = 3.14151617

# sentence = 'Pi is equal to {:.2f}'.format(pi)
# print(sentence)

# for i in range(1,11):
#     sentence = 'The value is {:03}'.format(i)
#     print(i)


# for i in range(1,11):
#     sentence = 'The value is {:02}'.format(i)
#     print(sentence)


# person = {'name': 'Hanks', 'age': 23}

# sentence = 'My name is {name} and I am {age} years old'.format(**person)
# print(sentence)


# sentence ='My name is {name} and I am {age} years old'.format(name='John', age=56)
# print(sentence)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Jack', 33)

# sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
# print(sentence)


# person = {'name': 'Jenn', 'age': 23}

# tag = 'h1'
# text = 'This is a headline'

# l = ['Jenn', 23]

# sentence ='My name is {0[0]} and I am {0[1]} years old'.format(l)
# print(sentence)

# sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person, person)
# print(sentence) 


# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)

# sentence ='<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)

# sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
# print(sentence)

# sentence = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])
# print(sentence)

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old'
# print(sentence)