# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printname(self):
#         print(self.fname, self.lname)
# x = Person('John','Doe')
# x.printname()
# class Studen(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(fname, lname)
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname,lname)
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printName(self):
#         print(self.fname, self.lname)
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(fname, lname)
# x = Student('Mike', 'Tysen')
# x.printName()
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printName(self):
#         print(self.firstname, self.lastname)
# class Student(Person):
#         def __init__(self, fname, lname):
#              super().__init__(fname, lname)
# x = Student('Mike', 'Olsen')
# x.printName()
# class Person:
#     def __init__(self, fname, lname,year):
#         self.fname= fname
#         self.lname = lname
#         self.year = year
#     def printName(self):
#         print(self.fname, self.lname, self.year)
# class Student(Person):
#     def __init__(self, fname, lname,year):
#         super().__init__(fname, lname, year)
#         self.graduationYear = year
# x = Student('Mike',' Janeson', 2019)
# print(x)
# class Person: 
#     def __init__(self,fname, lname):
#         self.fname =fname
#         self.lname = lname
#     def printname(self):
#         print(self.fname, self.lname)
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname,lname)
#         self.graduationyear = year
# x = Student('Mike', 'Janesen', 2010)
# print(x.graduationyear)
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#     def printName(self):
#         print(self.fname, self.lname)
# class Student(Person):
#     def __init__(self, fname, lname,year):
#         super().__init__(fname,lname)
#         self.graduationyear = year
#     def welcome(self):
#         print("Welcome to the class of", self.fname, self.lname , 'whose graduation year will be', self.graduationyear)
# x = Student('Mike', 'Jonson', 2023)
# x.welcome()