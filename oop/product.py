'''
Maintainable
Scalable
Easy to understand
Robust
Flexible

'''


'''
S - Single responsibility principle //class
O - Open/closed principle //inhertance
L - Liskov substitution principle // inhertance
I - Interfece segregation principle //ABC, abstract method
D - Dependecy inversion // abstraction, high level Mudule ont depend on low level

'''
class Category:
    pass

class Product:
    
    pass

class ProductValidator:
    pass

class ProductRepository:
    pass
class ProductService:
    pass
class Order:
    pass
class OrderValidator:
    pass
class OrderRepository:
    pass
class Payment:
    pass
class PaymentValidator:
    pass
class PaymentRepository:
    pass


desktop  = Category()
desktop = "Desktop"

laptop  = Category()
laptop = "Laptop"


p1 = Product()
p1.name  = "Lenevo core i 9"
p1.price = 50_000
p1.category = laptop

print(p1.__dict__)

p2 = Product()
p2.name  = "HP core i 9"
p2.price = 60_000
p2.category = laptop

print(p2.__dict__)
