


# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
#     for char in reverse('golf'):
#         print(char)

# class Reverse:
#     def __init__(self,data):
#         self.data = data
#         self.index = len(data)

#         def __iter__(self):
#             return self
        
#         def __next__(self):
#             if self.index == 0:
#                 raise StopIteration
#             self.index = self.index -1
#             return self.data[self.index]
# rev = Reverse('spam')
# print(iter(rev))
# for char in rev: 
#     print(char)


# from dataclasses import dataclass
# @dataclass
# class Employee:
#     name: str
#     dept: str
#     salary: int
# print(Employee('john', 'computer lab', 1000))

# class Mapping():
#     def __init__(self,iterable):
#         self.items_list =[]
#         self.__update(iterable)
# def update(self, iterable):
#     for item in iterable:
#         self.items_list.append(item)
#     __update = update
# class MappingSubclass(Mapping):
#     def update(self,keys,values):
#         for item in zip(keys, values):
#             self.items_list.append(item)


# class Bag:
#     def __init__(self):
#         self.data =[]
#     def add(self, x):
#         self.data.append(x)
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)

# class Warehouse:
#     purpose = 'storage'
#     region = 'west'

# w1 = Warehouse()
# print(w1.purpose, w1.region)
# w2 = Warehouse()
# w2.region = 'east'
# print(w2.purpose, w2.region)


# class Dog:
    
#     def __init__(self,name):
#         self.name = name
#         self.tricks  = []
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# d= Dog('Fido')
# e = Dog('Buddy')
# print(d.add_trick('roll over'))
# print(e.add_trick('play dead'))
# print(d.tricks)



# class Dog:
#     kind = 'canine'
#     def __init__(self, name):
#         self.name = name
# e =Dog('Fido')
# b = Dog('Buddy')
# print(e.kind)
# print(e.name)
# print(b.name)



# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = 'test spam'
#     do_local()
#     print("After local assignment:" , spam)
#     do_nonlocal()
#     print('After nonlocal assignment: ', spam)
#     do_global()
#     print('After global assignment:', spam)

# scope_test()
# print("In global scope:", spam)
