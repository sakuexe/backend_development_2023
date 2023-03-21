"""
    Iterators and Generators in Python
    ---
    - Iterator is an object that can be iterated upon.
    Meaning that you can traverse through all the values.
    An iterator is an object which implements the iterator
    protocol, which consists of the methods __iter__()
    and __next__()
    - Generators provide an easier way to do iterators
    using the yield keyword instead of return in the
    function definitions.
    Generator functions allow you to declare a function
    that behaves like an iterator. i.e. it can be used
    in a loop
"""

class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            # Stops iteration
            # doesn't give an error
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

a = [1, 2, 100, 30]
for i in Reverse(a):
    print(i)

# Generators
def reverse(data):
    """Generator iterating backwards"""
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse("spam"):
    print(char)

def fib():
    """
    Fibionacci sequence
    The generator remembers the state of variables
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
for x in range(10):
    print(next(f))

# Creating a Shopping cart software
from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    price: int  # in cents
    weight: int  # in grams
    description: str

@dataclass
class CartEntry:
    product: Product
    amount: int = 1

@dataclass
class ShoppingCart:
    cart: List[CartEntry]

    def find(self, product: Product):
        for i, item in enumerate(self.cart):
            if item.product == product:
                return i  # return index if found
        return -1  # not found

    def add(self, product: Product, amount: int = 1):
        i = self.find(product)
        if i >= 0:
            self.cart[i].amount += amount
        else:
            self.cart.append(CartEntry(product, amount))
    
    def remove(self, product: Product):
        i = self.find(product)
        if i >= 0:
            del self.cart[i]

    def get_number_of_items(self):
        return sum([item.amount for item in self.cart])

    def get_total_price(self):
        return sum([item.product.price*item.amount for item in self.cart])
        
    def get_total_weight(self):
        return sum([item.product.weight*item.amount for item in self.cart])

hammer = Product("Hammer", 2000, 1000, "Excellent at hammering")
nail = Product("Nail", 20, 10, "It is a 6 inch nail")
print(hammer)
cart = ShoppingCart([])
cart.add(hammer)
cart.add(nail, 50)
cart.add(nail, 20)
print("Contents:", cart)
print("Number of items:", cart.get_number_of_items())
print("Total Price:", cart.get_total_price())
print("Total Weight:", cart.get_total_weight())
cart.remove(nail)
print(cart)
