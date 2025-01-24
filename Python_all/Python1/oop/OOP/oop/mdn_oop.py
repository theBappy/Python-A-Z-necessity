class Shape: 
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
circel =Circle(5)
square = Square(4)

print('Area of circe:' , circel.area())
print('Area of square:', square.area())

shape = Shape()
print("Area of Shape:", shape.area())

# class MathOperations:
#     def add(self, *args):
#         total = sum(args)
#         return total
# math_obj = MathOperations()
# print(math_obj.add())
# print(math_obj.add(1))
# print(math_obj.add(1,2))
# print(math_obj.add(1,2,3))
   
# class MathOperations:
#     def add(self, a=0, b=0, c=0):
#         return a+b+c
# math_obj = MathOperations()

# print(math_obj.add())
# print(math_obj.add(1))
# print(math_obj.add(1,2))
# print(math_obj.add(1,2,3))


# from abc import ABC, abstractmethod

# class Electronic(ABC):
#     def __init__(self, name, brand, price, quantity):
#         self.name = name
#         self.brand = brand
#         self.__price = price
#         self.quantity = quantity
#         self.__discount = None

#     def set_discount(self, discount):
#         self.__discount = discount

#     def get_price(self):
#         if self.__discount:
#             return self.__price * (1-self.__discount)
#         return self.__price
    
#     @abstractmethod
#     def __repr__(self):
#         return f"Electronic(name='{self.name}', brand='{self.brand}', price={self.get_price()}, quantity={self.quantity})"
    
# class Laptop(Electronic):
#     def __init__(self, name, brand, price, quantity, processor):
#         super().__init__(name, brand, price, quantity)
#         self.processor = processor

#     def __repr__(self):
#         return f"Laptop, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, processor:{self.processor}"

# class Phone(Electronic):
#     def __init__(self, name, brand, price, quantity, display_size):
#         super().__init__(name, brand, price, quantity)
#         self.display_size =display_size
#     def __repr__(self):
#         return f"Phone, name: '{self.name}', brand:'{self.brand}', price:{self.get_price()}, display_size: {self.display_size}"

# phone1 = Phone("Smartphone", "Samsung", 1000, 2, 6.2)
# laptop1 = Laptop("Notebook", "HP", 800, 3, "Intel i5")
# print(phone1)
# print(laptop1)

# electronic1 = Electronic('Laptop', 'Dell' , 1200 , 5)
# electronic2 = Electronic('Smartphone', 'Samsung', 800, 10)
# electronic3 = Electronic('Headphones', 'Sony', 150, 20)

# laptop1 = Laptop('XPS 15', 'Dell', 1800, 25 ,'Inter Core i7')
# laptop1.set_discount(0.15)

# phone1 = Phone('Galaxy $20', 'Samsung', 800, 215, '6.2 inches')
# phone1.set_discount(0.22)

# print(laptop1)
# print(phone1)

# one_laptop = Electronic("Laptop", "Dell", 1200, 1)

# multi_laptops = Electronic("Laptop", "Acer", 1500, 10)
# multi_laptops.set_discount(0.20)

# print(one_laptop.get_price())
# print(multi_laptops.get_price())
# print(one_laptop)
# print(multi_laptops)

# print(electronic1.name)
# print(electronic1.brand)
# print(electronic1.price)
# print(electronic1.quantity)
# print(electronic1.__discount)
# print(electronic1)

# print(electronic1)
# print(electronic2)
# print(electronic3)

