"""
    Scopes, Own Modules, Packages and Imports in Python
    ---
    - Any name declared inside a function is local unless
    preceeded with keyword nonlocal (enclosing scope)
    or global.
    Local is usually better than Global.
    It is faster and creates less pollution in the
    global name-space
    ---
    Additional Information
    - Python Modules and Packages - An introduction
    https://realpython.com/python-modules-packages/
    - Python tutorial about modules
    https://docs.python.org/3/tutorial/modules.html
"""

global_var = 2  # Global variable

def f(x):  # this parameter is local
    x = x * 2  # this is a local version
    y = x * 2  # this is also local
    return y

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assingment:", spam)
    do_nonlocal()
    print("After nonlocal assingment", spam)
    do_global()
    print("After global assingment", spam)

scope_test()
print("In global scope:", spam)

# Modules
# Every Python file (.py) is automatically a module
# with its own name space
# Before writing your own code, study / search official modules
# Do not create a python file with the following:
# - åäö
# - Python keywords: e.g. def, return, if, class, while
# - spaces or capital letters
# - built in functions in python: e.g.list, min, max, input
# - a module in the standard library: e.g. random, math, sys

# main way of importing modules
import collections

# this is not recommended, since it will cause overrides
# avoid at all costs
from mypackage.mymath import *

# more recommended way of importing modules
from math import radians, pow, sin

# if you want to change the name of the module
# do it with the as keyword
from collections import deque as dq

# Python Packages
"""
    A directory with Python code and __init__.py is a package.
    Packages can contain subfolders and subpackages.
    Folders without __init__.py are ignored, but
    __init__.py can be empty
"""

# import package.module
# package.module.func()
# from package import module
# module.func()

# Three ways of importing packages
import mypackage.mymath
numbers = (1, 3.14, 2)
print("Average", mypackage.mymath.average(numbers))

from mypackage import mymath
print("Average:", mymath.average(numbers))

from mypackage.mymath import average
print("Average:", average(numbers))

# You couldve also just used the statistics package
# this gets the average too
from statistics import mean
print(mean(numbers))
