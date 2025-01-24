# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}({self.age})"
#     def myfunc(self):
#         print("Hello my name is "+ self.name)
# p1 = Person('John', 45)
# print(p1.name)
# print(p1.age)
# print(p1)
# p1.myfunc()

# class Person:
#     def __init__(mysilliobject, name, age):
#         mysilliobject.name = name
#         mysilliobject.age = age
#     def myfunc(abc):
#         print("Hello my name is " + abc.name)
# p1 = Person('David', 45)
# p1.age = 56
# print(p1.age)
# del p1.age
# print(p1.age)
# del p1
# p1.myfunc()

# class Person:
#     pass

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printname(self):
#         print(self.fname, self.lname)
# x = Person('John', 'Doe')
# x.printname()

# class Person: 
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printname(self):
#         print(self.fname, self.lname)
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationYear = year
#     def welcome(self):
#         print("Welcome", self.fname, self.lname, "to the class of ", self.graduationYear)

# # x = Person('John','Doe')
# # x.printname()
# y = Student('Mike', 'Tysen', 2019)
# y.welcome()

# mytuple = ('apple', 'banana', 'cherry')
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = 'banana'
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mytuple =('apple', 'banana', 'cherry')
# for x in mytuple:
#     print(x)

# mystr = 'banana'
# for x in mystr:
#     print(x)

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# myclass = MyNumbers()
# myiter =iter(myclass)

# for x in myiter:
#     print(x)

# x = 'Hello world'
# print(len(x))
# mytuple = ("apple", "banana", "cherry")
# print(len(mytuple))

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive")
# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Sail")

# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Flying")

# car1 = Car('Ford', 'Mustang')
# boat1 = Boat("Ibiza", 'Touring 345')
# plane1 = Plane('Boeing', '747')

# for x in (car1, boat1, plane1):
#     x.move()

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move!")
# class Car(Vehicle):
#     pass
# class Boat(Vehicle):
#     def move(self):
#         print("Sail")
# class Plane(Vehicle):
#     def move(self):
#         print("Flying")

# car1 = Car('Ford', 'Mustang')
# boat1 = Boat("Ibiza", 'Touring 345')
# plane1 = Plane('Boeing', '747')

# for x in (car1, boat1, plane1):
#     print(x.model)
#     print(x.brand)
#     x.move()



    

