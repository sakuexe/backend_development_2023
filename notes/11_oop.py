"""
    Object Oriented Programming in Python
    ---
    - Class = Definition of data and methods
    - Object = Instance of a Class
    - Instance = Individual
    - Method = Function attached to an instance of a class
    - Encapsulation = Hiding data
    - Inheritance = Copying features from parent and it's parents
    - Child Class = Inherited from a parent class
    - Member / Attribute of object = feature of an object
    - Method Overloading = Method with the same name,
    but with different number or type of parameters
    - Operator Overloading = Change meaning of an operator
    ---
    Additional Information
    - Python tutorial about classes
    https://docs.python.org/3/tutorial/classes.html
    - RealPython - Tutorial on OOP
    https://realpython.com/python3-object-oriented-programming/
"""

# Syntax for creating classes:
# class SubClassName(ParentClass1, ParentClass2, ...):

# Everything is public by default in Python
# _ in front of name = protected, children can see the data
# __ in front of name = private - not even children can see data

# Special methods use __specialname__
# __init__(self, parameters) - constructor
# __str__(self) - return string representation of object. e.g. toString()

# Python doesn't use "new" keywords in creation of an object
# new_object = ClassName(parameters)
# changing and reading public attributes is trivial
# new_object.attribute = new_value
# print(new_object.attribute)

class Person:
    # self refers to current instance of class
    # just like 'this' in C#
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person('{self.name}', {self.age})"

class Student(Person):
    def __init__(self, name, age, id_no):
        # super = parent of class
        super().__init__(name, age)
        self.id_no = id_no
    def __str__(self):
        return f"Student('{self.name}', {self.age}, '{self.id_no}')"

jack = Student("Jack Student", 25, "10100")
print(jack)
jack.age += 1
print(jack)

jill = Student("Jill Student", 23, "10101")
jill.name = "Jill Taylor"
print(jill)
# You can add new attributes dynamically
jill.address = "Example Street 123"
print(jill.address)

people = [jack, jill]

for person in people:
    person.age += 1
    print(person.name, person.age, end="")
    if hasattr(person, "address"):
        print("", person.address)
    else:
        print()

# Using Slots to Speed Up Classes
# If small memory and fast execution is your main
# worry and you know all your instance attributes in advance,
# consider defining them at class level using:
__slots__ = ['attribute', 'attribute2']

# No slots
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
m = MyClass("name", "id")
m.age = 100  # You can add new identifiers
print(m.age)

# Same with slots
class MyClass2(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
m = MyClass2("name", "id")
# This will fail, since attribute is not in slots
# m.age = 100

class Account:
    """
    Bank account, which has balance as cents
    """
    def __init__(self, balance) -> None:
        self.balance = balance  # public by default
    def __str__(self):
        return f"Account({self.balance})"

a = Account(500)  # 5 euros
print(a)
a.balance += 1000  # add 10 euros
print(a)
# You can add new attributes to objects and classes
# Although it is not reccomended, as it makes it
# very confusing for other programmers
a.type = "saving"
print(a.type)

class SafeAccount:
    """
    Bank account, which has balance as cents
    But this time it uses slots
    """
    __slots__ = ("balance", )  # tuple, which defines attributes

    def __init__(self, balance) -> None:
        self.balance = balance  # public by default
    def __str__(self):
        return f"Account({self.balance})"

# The following will fail now
# a.type = "saving"
# print(a.type)

class PrivateAccount:
    """
    Bank account, which has balance as cents
    But this time it uses slots
    And now the attribute is private with the use of "__"
    """
    __slots__ = ("__balance", )  # tuple, which defines attributes

    def __init__(self, balance) -> None:
        self.__balance = balance  # public by default
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    def draw(self, amount):
        self.__balance = max(self.__balance-amount, 0)
        return self.__balance
    def __str__(self):
        return f"Account({self.__balance})"

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real}+{self.imag}i"

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

x = Complex(1, 2)
y = Complex(2, 4)
x = x + y
print(x)  # calling __str__ for human readable version
# calling repr for string which allows to recreate object
print(repr(x))

# You could always make an empty class
# but Why would you? - Dunno, still pretty neat
class Empty: pass

e = Empty()
e.name = "example"
e.age = 12
print(e.age)
print(e.name)
del e.age
