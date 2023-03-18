"""
    8 - Functions, Lambdas and List Comprehension in Python
    ---
    Additional information
    - Defining Your Own Python Function
    https://realpython.com/defining-your-own-python-function/
    - How to use Python Lambda Function
    https://realpython.com/python-lambda/
    - When to use List Comprehension in Python
    https://realpython.com/list-comprehension-python/
"""

def is_palindrome(string: str) -> bool:
    string = string.lower()
    reverse: str = string[::-1]
    return reverse == string

# you can add functions into variables
check_palindrome = is_palindrome
print(check_palindrome("saippuakauppias"))
print(check_palindrome("PekKaKauPpA"))

# function which takes arguments and returns a value
def inches_to_cm(inch):
    return inch * 2.54
# function which takes arguments and doesn't return a value
def print_many(s, n):
    for i in range(n):
        print(s)
# function which doesn't take arguments and returns a value
def tell_secret():
    return "The secret is you"
# function which doesn't take arguments and doesn't return a value
# very rarely used, maybe in initialization or ending of processes
def the_end():
    print("This is the end")

# default values can be added in python in the same way as in Javascript
# by using the = sign after the argument
def print_multiple(string, n=5):
    for i in range(n):
        print(string)

# Both ways work, since the second argument has a default value
# So it can be used as an optional argument
print_multiple("CLICK HERE - IMPORTANT INFO")
print_multiple("Not as important info tbh - no need to click", 2)

# Variable amount of function arguments
# *n returns a tuple of given arguments
def mysum(*n):
    total = 0
    for number in n:
        total += number
    return total

# Both of these will work
print(mysum(2, 4, 4, 5, 6))  # 21
print(mysum(2, 4))  # 6

# Variable amount of keyword arguments
# **parameters return a dictionary of arguments
def login(**parameters):
    if "user" in parameters:
        print("User name:", parameters.get("user"))
    if "password" in parameters:
        print("Password:", parameters.get("password"))

# both of these work, since the arguments don't
# need to be called in order
login(user="root", password="admin")
login(password="admin", user="root")
# but the following would not work, because it doesn't get given
# any positional arguments
# login("root", "password")

# Lambda

# syntax:
# lambda arguments: expression
# is pretty much the same as:
# def anonymous(arguments):
#     return expression

lambda_func = lambda x: x+1
print(lambda_func(5))  # 6

product = lambda a, b: a*b
print(product(3,2))  # 6

my_abs = lambda x: x if x >= 0 else -x
print(my_abs(-5))  # 5

# Functions returning functions
def make_adder(n):
    def adder(x):
        return x+n
    return adder
# More concise version using lambda
def make_adder2(n):
    return lambda x: x+n

inc2 = make_adder2(2)
print(inc2(4))

# List Comprehensions
# provides a concise way to create lists
# it consists of brackets containing an expression
# followed by a for clause, then 0.. N for or if clauses

numbers = [1,2,4,10,-5,7]
squared = [number * number for number in numbers]
odd = [num for num in numbers if num%2 != 0]
string_nums = ['1','2','3','100','-15']
int_list = [int(i) for i in string_nums]
big_ints = [int(i) for i in string_nums if len(i) >= 3]

names = ['charLES', 'Carlos', 'MAX', 'ChecO', 'x']
lower_names = [s.lower() for s in names]
upper_names = [s.upper() for s in names if len(s) > 1]
print(lower_names)
print(upper_names)

# Functional programming - map, reduce, filter
# in Python 3 you must import reduce from functools
from functools import reduce

# map(funtion, sequence)
# applies a function to all items of a sequence
underscore_names = map(lambda s: "_"+s+"_", names)
# map needs to be converted to a list or iterated through
# with loops
print(list(underscore_names))

# filter(function, sequence)
# creates a new sequence consisting of those items,
# which the function returned true
ages = [1, 23, 0, 100, 15, 18, 52, 3, 50, 35]
legal_ages = filter(lambda age: age >= 18, ages)
print(list(legal_ages))

# reduce(function, sequence)
# reduce the sequence to one result,
# by applying given function to list
# - Needs to be imported from functools
d = reduce(lambda x, y: x + y, ages)  # calculate sum
e = reduce(lambda x, y: x + y,\
           map(lambda x: x * x, filter(lambda x: x % 2 == 0, ages)))
# same with list Comprehension
sum([x * x for x in ages if x % 2 == 0])

# Recursion
# A function calling itself. Useful for some algorithms

# example of loop using tail recursion
def f(n):
    print(n)
    if n>0: f(n-1)
print(f(10))

def factorial(n):
    if n == 0: return 1
    if n > 0: return n * factorial(n-1)
print(factorial(6))  # 6*5*4*3*2*1 = 720
