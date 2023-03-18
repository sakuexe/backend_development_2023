"""
    Dictionaries in Python
    ---
    Dictionary is a built in mapping type, which maps immutable values
    (numbers, strings, tuple) to arbitary objects
    Dictionaries are mutable
    Syntax: {key: value}
    Implemented as a hash table
    ---
    Additional information:
    - Python Data Structures
    https://docs.python.org/3/tutorial/datastructures.html
    - Python library reference - Mapping types - dict
    https://docs.python.org/3/library/stdtypes.html#typesmapping
"""

users = {}
users["John"] = 24
users["Markku"] = 45
users["Charles"] = 26
print(users)
# You can change the values easily with key values
users["Markku"] += 1

obj1 = {"name": "mouse", "price": 5995}
obj2 = {"name": "keyboard", "price": 15995}
obj3 = {"name": "display", "price": 65995}

products = [obj1, obj2, obj3]
# Iterate through a list of objects like this
for product in products:
    print(product["name"], product["price"])

# test if something can be found in a dictionary
# This is very fast and scales up well. O(1)
print("John" in users) # True
print("Jonathan" in users) # False

# Clear a dictionary or remove an element
# users.clear()
del users["John"]
# You can also use the del keyword for deleting variables!
unused_var = "Just something"
del unused_var

# iterate through dictionaries with this useful trick
animals: dict = {"cat": "kissa", "dog": "koira", "monkey": "apina"}
for key, value in animals.items():
    print(key, "=", value)

phone_book: dict = {
    "Jack Smith": "+358 57 757 1223",
    "Charles Leclerc": "+358 57 757 1223",
    "Max Verstappen": "+358 51 717 1423",
    "Carlos Sainz": "+358 51 781 1908",
}
for person, number in phone_book.items():
    print(person, "- phone:", number)

# You can use dir to check all currently available objects
print(dir())
# You can check some documentation of the objects
print(phone_book.__doc__)
import math
print(math.sin.__doc__)

# You can use vars() to check variables and their values
# In a dictionary datatype
print(vars())
