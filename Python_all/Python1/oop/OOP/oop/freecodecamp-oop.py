class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    
rect = Rectangle(5,3)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
# print(rect.__length)



# class Base:
#     def __init__(self):
#         self.a = 'GeeksforGeeks'
#         self.__c = "GeeksByGeks"
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of the base class:")
#         print(self.__c)
# obj1 = Base()
# print(obj1.a)



# class Bird:
#     def intro(self):
#         print('There are many types of birds.')

#     def flight(self):
#         print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):
#     def flight(self):
#         print("Sparrow can fly")
# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()



# class Person(object):
#     def __init__(self, name, idnunmber):
#         self.name = name
#         self.idnumber = idnunmber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("Id number: {}".format(self.idnumber))

# class Employee(Person):
#     def __init__(self, name, idnunmber, salary, post):
#         super().__init__(name, idnunmber)
#         self.salary = salary
#         self.post = post

#         def details(self):
#             print("My name is {}".format(self.name))
#             print("My post is {}".format(self.post))
#             print("My salary is: {}".format(self.salary))

# a = Employee('Rahul', 898989, 340000, 'Intern')

# a.display()
# a.details()




# class Dog:
#     attr1 = 'mammal'

#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print("My name is {}".format(self.name))
# Rodger = Dog('Rodger')
# Tommy = Dog('Tommy')
# Rodger.speak()
# Tommy.speak()

# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is a{}".format(Tommy.__class__.attr1))
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))
# print(Rodger.name)
# print(Tommy.name)
    



# class Dog:
#     pass

# class ParentClass:
#     def call_me(self):
#         print('I am parent class')
# class ChildClass(ParentClass):
#     def call_me(self):
#         print('I am child class')
#         super().call_me()
# pobj = ParentClass()
# cobj = ChildClass()
# print(pobj.call_me())
# print(cobj.call_me())

# class OverloadingDemo:
#     def add(self, x, y):
#         print(x+y)

#     def add(self, x,y, z):
#         print(x+y+z)
# obs = OverloadingDemo()
# print(obs.add(2,3,5))


# from abc import ABC, abstractmethod
# class Book:
#     def __init__(self, title, quantity, author, price):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.__price = price
#         self.__discount = 0.10
    
#     def set_discount(self, discount):
#         self.__discount = discount
#     def get_price(self):
#         if self.__discount:
#             return self.__price * (1- self.__discount)
#     @abstractmethod
#     def __repr__(self):
#         return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price:{self.author}"
# class Novel(Book):
#     def __init__(self, title, quantity, author, price, pages):
#         super().__init__(title, quantity, author, price)
#         self.pages = pages
# class Academic(Book):
#     def __init__(self, title, quantity, author, price, branch):
#         super().__init__(title, quantity, author, price)
#         self.branch = branch
#     def __repr__(self):
#         return f"Book: {self.title}, Branch:{self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price:{self.get_price()}"
        
# novel1 = Novel('Two states', 20, 'Chetan Bhagat', 200, 187)
# novel1.set_discount(0.20)

# academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

# print(novel1)
# print(academic1)

# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)

# single_book = Book('Two states', 1, 'Chetan Bhagat', 200)

# bulk_books = Book('Two states', 25, 'Chetan Bhagat', 200)
# bulk_books.set_discount(0.20)

# print(single_book.get_price())
# print(bulk_books.get_price())
# print(single_book)
# print(bulk_books)

# print(book1.title)
# print(book1.quantity)
# print(book1.author)
# print(book1.price)
# print(book1.__discount)

# print(book1)
# print(book2)
# print(book3)