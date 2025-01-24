# class Mixin1(object):
#     def test(self):
#         print('Mixin1')
# class Mixin2(object):
#     def test(self):
#         print(Mixin2)
# class MyClass(Mixin1, Mixin2):
#     pass
# obj = MyClass()
# obj.test()

# class Singleton:
#     _instance = None

#     @staticmethod
#     def getInstance():
#         if Singleton._instance == None:
#             Singleton()
#         return Singleton._instance
#     def __init__(self):
#         if  Singleton._instance != None:
#             raise Exception("this class is a singleton")
#         else:
#             Singleton._instance = self
# s = Singleton.getInstance()
# print(s)



# class MyClass:
#     @staticmethod
#     def method():
#         return "Static method called"
#     @classmethod
#     def classMethod(cls):
#         return 'Class method called'
# print(MyClass.method())
# print(MyClass.classMethod())


# class Parent1:
#     def method1(self):
#         return "Parent1's method called"
# class Parent2:
#     def method2(self):
#         return "Parent2's method called"
# class Child(Parent1, Parent2):
#     pass
# c = Child()
# print(c.method1())
# print(c.method2())

# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
# class Employee:
#     def __init__(self,name, salary):
#         self.name = name
#         self.salary = salary
# s = Salary(15000,5000)
# e = Employee('Ashwin', s)
# print(e.salary.pay)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#     def __repr__(self):
#         return f"Person('{self.name}', {self.age})"
# p = Person('John', 30)
# print(str(p))
# print(repr(p))

# class Mango:
#     def __init__(self,x):
#         self.x = x
#     def __add__(self,y):
#         return self.x + y.x
# obj1 = Mango(7)
# obj2 = Mango('mangoes')
# print(obj1+obj2)

# class MyClass:
#     @classmethod
#     def class_method(cls):
#         return 'class method called'
#     @staticmethod
#     def static_method():
#         return 'static method called'
# print(MyClass.class_method())
# print(MyClass.static_method())


# from abc import ABC, abstractmethod
# class AbstractAnimal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
# class Dog(AbstractAnimal):
#     def speak(self):
#         return 'boww boww'
# dog = Dog()
# print(dog.speak())


# from collections.abc import Iterable
# def get_length(item):
#     if isinstance(item, Iterable):
#         return len(item)
#     else:
#         return "not iterable"
# print(get_length('hello'))
# print(get_length([1,2,3]))
# print(get_length(123))

# class MyClass:
#     def __init__(self):
#         self.public = "public"
#         self._protected = "protected"
#         self.__private = "private"
# obj = MyClass()
# print(obj.public)
# print(obj._protected)
# print(obj.__private)

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def radius(self):
#         return self._radius
#     @radius.setter
#     def radius(self, value):
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError("Radius must be positive")
# circle = Circle(5)
# print(circle.radius)
# circle.radius =10
# print(circle.radius)

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         return f"{self.name} says hello"
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
# dog = Dog("Charlie", "Bulldog")
# print(dog.breed)


# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return f"{self.name} says hello"
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks"
# dog = Dog("Charlie")
# print(dog.speak())


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         return f"{self.name} says hello"
# dog = Animal('Charlie')
# print(dog.speak())


# class Bank:
#     def __init__(self):
#         self.customers = {}
#     def create_account(self, account_number, initial_balance=0):
#         if account_number in self.customers:
#             print("account number alerady exists")
#         else:
#             self.customers[account_number] = initial_balance
#             print("account created successfully")
#     def make_deposit(self, account_number, amount):
#         if account_number in self.customers:
#             self.customers[account_number] += amount
#             print('Deposti successful')
#         else:
#             print('account number  does not exist')
#     def make_withdrawl(self, account_number, amount):
#         if account_number in self.customers:
#             if self.customers[account_number] >=amount:
#                 self.customers[account_number] -= amount
#                 print('withdrawal successful')
#             else:
#                 print('insufficient funds')
#         else:
#             print('account number does not exist')
#     def check_balance(self, account_number):
#         if account_number in self.customers:
#             balance = self.customers[account_number]
#             print('account balance: {balance}')
#         else:
#             print('account does not exists')

# class Queue:
#     def __init__(self):
#         self.items = []
#     def enqueue(self,item):
#         self.items.append(item)
#     def debeque(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             raise IndexError("cannot debequre from an empty quequ")
        
#     def is_empty(self):
#         return len(self.items) ==0
# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)
# print("Current queue: ", queue.items)
# debequed_items = queue.debeque()
# print("debequed items: ", debequed_items)
# print("updated queue: ", queue.items)

# class ShoppingCart:
#     def __init__(self):
#         self.items =[]
#     def add_items(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break
#     def calculate_total(self):
#         total = 0
#         for item in self.items: 
#             total += item[1]
#         return total
# cart = ShoppingCart()
# cart.add_items('papaya', 200)
# cart.add_items('guava', 300)
# cart.add_items('orange', 150)

# print("Curretn items in cart: ")
# for item in cart.items:
#     print(item[0],'-', item[1])
# total_qty = cart.calculate_total()
# print("total quantity", total_qty)
# cart.remove_item('orange')
# print('\nUpdated items in cart after removing orange:')
# for item in cart.items:
#     print(item[0],'-',item[1])
# total_qty = cart.calculate_total()
# print("total quantity: ", total_qty)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end="")
#         print()
#     def insert(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#     def delete(self,data):
#         if not self.head:
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         current = self.head
#         prev = Node
#         while current and current.data != data:
#             prev = current
#             current = current.next
#         if current:
#             prev.next = current.next
# linked_list = LinkedList()
# linked_list.insert(1)
# linked_list.insert(2)
# linked_list.insert(3)
# linked_list.insert(4)

# print("Initial linked list: ")
# linked_list.display()
# linked_list.delete(2)
# linked_list.display()
 

# class Stack:
#     def __init__(self):
#         self.items =[]
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return 'cannot pop from an empty stack'
#     def is_empty(self):
#         return len(self.items) == 0
#     def size(self):
#         return len(self.items)
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return 'Empty stack'
# stack = Stack()
# stack.push(5)
# stack.push(8)
# stack.push(7)
# stack.push(0)
# stack.push(1)
# print(stack.size())
# print(stack.peek())
        

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
#     def __str__(self):
#         return str(self.value)
    
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self._insert_recursive(self.root, value)
#     def _insert_recursive(self, node, value):
#         if value <  node.value:
#             if node.left is None:
#                 node.left = Node(value)
#             else:
#                 self._insert_recursive(node.left, value)
#         elif value > node.value:
#             if node.right is None:
#                 node.right = Node(value)
#             else:
#                 self._insert_recursive(node.right, value)
#     def search(self, value):
#         return self._search_recursive(self.root, value)
#     def _search_recursive(self, node, value):
#         if node is None or node.value == value:
#             return node
#         if value < node.value:
#             return self._search_recursive(node.left, value)
#         else:
#             return self._search_recursive(node.right, value)
# bst = BinarySearchTree()
# bst.insert(4)
# bst.insert(7)
# bst.insert(3)
# bst.insert(6)
# bst.insert(8)
# bst.insert(2)
# bst.insert(5)
# print("Searching for elements:")
# print(bst.search(4))
# print(bst.search(7))
# print(bst.search(9))


# import math
# class Shape: 
#     def calculate_area(self):
#         pass
#     def calculate_perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return  math.pi * self.radius**2
#     def calculate_perimeter(self):
#         return 2* math.pi * self.radius
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def calculate_area(self):
#         return self.length * self.width
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)
# class Triangle(Shape):
#     def __init__(self, base, height, side1, side2, side3):
#         self.base = base
#         self.height = height
#         self.side1 = side1
#         self.side2= side2
#         self.side3 = side3

#     def calculate_area(self):
#         return 0.5 * self.base * self.height
#     def calculate_perimeter(self):
#         return self.side1 + self.side2 + self.side3
    
# r = 7
# circle = Circle(r)
# circle_area = circle.calculate_area()
# circcle_perimeter = circle.calculate_perimeter()
# print(circle.__dict__)
# print(circle_area)
# print(circcle_perimeter)  
        
        
# from datetime import date
# class Person:
#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = dob
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.dob.year
#         if today < date(today.year , self.dob.month, self.dob.day):
#             age -= 1
#         return age
# person1 = Person('John', "France", date(1996,10,19))
# print(person1.name)
# print(person1.country)
# print(person1.dob)
# print(person1.calculate_age())

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def calculate_circle_area(self):
#         return math.pi * self.radius**2
#     def calculate_circle_perimeter(self):
#         return 2 * math.pi * self.radius

# circle = Circle(5)
# area = circle.calculate_circle_area()
# permiter = circle.calculate_circle_perimeter()
# print(area)
# print(permiter)
        


# class Calculator:
#     def add(self, x, y):
#         return x+y
#     def substract(self, x, y):
#         return x - y
#     def multiple(self, x, y):
#         return x*y
#     def divide(self, x, y ):
#         if y != 0:
#             return x/y
#         else:
#             return("Cannot divide by zero")
# calculator = Calculator()
# print(calculator.add(8,9))
# print(calculator.substract(9,16))
# print(calculator.multiple(8,9))
# print(calculator.divide(8,9))
# print(calculator.divide(9,0))
    


# class ShoppingCart:
#     def __init__(self):
#         self.items =[]
    
#     def add_item(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)
    
#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break
#     def calculate_total(self):
#         total =0
#         for item in self.items:
#             total += item[1]
#         return total

# cart =ShoppingCart()
# cart.add_item('Papaya', 100)
# cart.add_item('Guava', 200)
# cart.add_item('Orange', 150)
# print("Current items in cart:")
# for item in cart.items:
#     print(item[0], "-", item[1])
# total_qty = cart.calculate_total()
# print("Total quantity:", total_qty)
# cart.remove_item('Orange')
# print("\nUpdated Items in cart after removing orange:")
# for item in cart.items:
#     print(item[0],'-',item[1])
# total_qty = cart.calculate_total()
# print("Total quantity: ", total_qty)


# class Bank:
#     def __init__(self):
#         self.customers ={}
#     def create_account(self, account_number, initial_balance=0):
#         if account_number in self.customers:
#             print('Account number already exists')

#         else:
#             self.customers[account_number] = initial_balance
#             print('Account number created successfully')
    
#     def make_deposit(self, account_number, amount):
#         if account_number in self.customers:
#             self.customers[account_number] += amount
#             print("Deposit successful")
#         else: 
#             print("Account number does not exist")

#     def make_withdrawl(self, account_number, amount):
#         if account_number in self.customers:
#             if self.customers[account_number] >= amount:
#                 self.customers[account_number] -= amount
#                 print('Withdrawl successful')
#             else:
#                 print('Insufficient funds.')
#         else:
#             print('Account number does not exist')

#     def check_balance(self, account_number):
#         if account_number in self.customers:
#             balance = self.customers[account_number]
#             print(f"Account balance: {balance}")
#         else:
#             print("Account number does not exist")

# bank = Bank()
# acno1 = "SB-123"
# damt1 = 1000
# print("New a/c no: ", acno1, "Deposit amount: ", damt1)
# bank.create_account(acno1,damt1)
# wamt1 = 600
# print("\nDeposit Rs.", wamt1, "to A/C no:", acno1)
# bank.make_deposit(acno1, wamt1)
# print("A/C no:", acno1)
# bank.check_balance(acno1)
        
        
