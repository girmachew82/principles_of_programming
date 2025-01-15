import datetime
class Category:
    def __init__(self, name, datetime, user_id):
        self.name = name
        self.datetime = datetime
        self.user_id = user_id


class Product:
    def __init__(self, category, name, price, quantity):
        self.category = category
        self.name = name
        self.price = price
        self.quantity = quantity

    def cart(self, name, quantity):
        self.name = name
        self.quantity = quantity
        if not name or not quantity:
            raise ValueError("Name and quantity are required")
        else:
            print(f"{name} with {quantity}")
    
    def report(self, category, name, purchased_quantity, remaining_quantity):
        self.category = category
        self.name = name
        self.purchased_quantity = purchased_quantity
        self.remaining_quantity = remaining_quantity



laptop = Category("Laptop", datetime.datetime.now(),1)
print(laptop.__dict__)


desktop = Category("Desktop",datetime.datetime.now(),2)
print(desktop.__dict__)


p1 = Product(laptop.name, "Lenevo core i 9",60_0000, 9)
print(p1.__dict__)

