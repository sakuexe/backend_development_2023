"""
    Type Hints and Data Classes in Python
    ---
    Type Hints = Static Type Checking for Python
    The static checker tool for Python is called MyPy
    http://mypy-lang.org/
    It will catch type errors from your own type hints
    ---
    Additional Information
    - Typing Documentation
    https://docs.python.org/3/library/typing.html
    - Type hints cheat sheet (VERY GOOD)
    https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
    - Extensive typing tutorial for Python
    https://realpython.com/python-type-checking/
    - Data classes tutorial
    https://realpython.com/python-data-classes/
"""
from __future__ import annotations

weigth: int  # variable: type
weigth: int = 10  # variable: type = value

# strings: List[str]  # collection: CollectionName[type...]
# def func(arg1: type, arg: type = value) -> returnval:
def square(x: float) -> float:
    return x*x

# built in types: int, float, bool, str
# The following must be imported from typing module
import typing
# Collections: List, Tuple, Set, Dict, Sequence
# Special: Any, Optional, Generic, Union, Callable, Iterator
# Mapping, TypeVar

from typing import List, Dict, Tuple, Union, Any

# The typing hint is only a HINT. Will not throw errors in runtime
# but depending on the editor, LSP might show an error in editing
def is_negative(x: float) -> bool:
    """
    Python automatically converts ints to floats
    """
    return x < 0

def print_many(s: Union[str, int, float], n: int = 5) -> None:
    for i in range(n):
        print(s)

def multiply_list(a: List[float], n: float) -> List[float]:
    return [n*i for i in a]

# key is string, value can be Any
d: Dict[str, Any] = {"key": "value", "key2": ("tuple",), "key3": 13}
# this will not work thanks to the typing, throws an error in editing
# but will not throw error in runtime, with python's normal interpeter
# d[123] = "bug"
print(is_negative(4))
# with the type assists, the LSP will notice the bug when function is called
# print(is_negative("bug"))
print_many(5)
print(multiply_list([1,2.5,4], 2.5))

# Data Classes and Type Checking Annotations
# Data Classes do have some gotchas though
# like for example, if you inherit a class with
# default values, it might crash
from dataclasses import dataclass

# Dataclass automatically creates the constructors
@dataclass
class Person:
    name: str
    age: int
    # age: int = 18 - gives error
    # since the default value isn't the last attribute

# and even inheritance
@dataclass
class Student(Person):
    id_no: str

charles = Student("Charles Leclerc", 25, "10100")
charles.age += 1
print(charles)

# Remake the Comlex class from the line 158 of the 11_oop.py file
# using dataclasses
# from __future__ import annotations - at the start of the file
# this is done for forward referencing

# This is incredible! So so so much cleaner
@dataclass
class Complex:
    real: float
    imag: float

    def __add__(self, other: Complex) -> Complex:
        return Complex(self.real + other.real, self.imag + other.imag)

x = Complex(1, 2)
y = Complex(2, 4)
x = x + y
print(x)  # calling __str__ for human readable version
