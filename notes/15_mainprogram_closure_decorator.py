"""
    Main Program, Closures and Decorators in Python
    ---
    - If you import a python file you created, it will
    run it as well. If you are planning to make a library
    and not a main program file, then consider using:
    if __name__ == "__main__":
    - What is a closure? - it needs to fulfill the following
    1. Closure is a nested function (inner function inside an outer one)
    2. The nested inner function must refer to a value defined in the
    enclosing function.
    3. The enclosing function must return the nested inner function
    ---
    Additional Information
    - Primer on Python Decorators
    https://realpython.com/primer-on-python-decorators/
    - Python inner functions - What are they good for?
    https://realpython.com/inner-functions-what-are-they-good-for/
"""

# by using this line, you make sure that the code following it
# will only be run when the file is run directly
# and not when it is being imported as a module
if __name__ == "__main__":
    print("We are running this file")

# Closure
"""
    - A closure is an instance of a function, a value, whose
    non-local variables have been bound either to values
    or to storage locations
    - A closure is a value like any other value. It does not
    need to be assigned to a variable and can be instead be used
    directly or so called "anonymous closure"
    - Closures can avoid the use of global values and provides
    some form of data hiding. It can also prive an elegant
    solution to the problem, instead of making a class.
    If you need a lot of attributes and functionality,
    class is usually a better solution
"""

# Closure Example
def make_multiplier(x):  # outer / enclosing function
    def multiplier(y):  # inner / nested function
        return x*y
    return multiplier

# always multiply by ten
mul10 = make_multiplier(10)  # mul10 is the closure
print(mul10(5))  # 50
print(mul10(10))  # 100
# always multiply by two
mul2 = make_multiplier(2)  # mul2 is the closure
print(mul2(10))  # 20

# Basically you can use closures like instances of a class
# it is not that complicated when you think about it like that

# Decorators
"""
    - Decorators add functionality to an existing code, using closures
    - This is also called metaprogramming because a part of the
    program tries to modify another part of the program at compile time
"""

# Defining and using decorators
# def decorator_name(func):
#     # takes any amount of arguments
#     # and any amount of keyword arguments
#     def inner(*args, **kwargs):
#         # Decorator does its job here
#     return inner

# @decorator_name
# def something_else():
#     # TODO

# Decorator Example
def safe_divide(func):
    def inner(a, b):
        print("Trying to divide", a, "and", b)
        if b == 0:
            print("Division by Zero")
            return
        return func(a,b)
    return inner

@safe_divide
def divide(a, b):
    print(a / b)

divide(7, 2)
divide(5, 0)

# Another example of a decorator function
from time import perf_counter

def timeit(func):
    """
    Calculates the time that it took for the given function
    to execute. In seconds
    """
    def timeit_inner(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        time_taken = perf_counter() - start_time
        print(f"Function: {func.__name__}({args} {kwargs}) \
        Took {time_taken:.4f} seconds")
        return result
    return timeit_inner

@timeit
def calculate_something(num):
        """
        an example function that returns sum of all numbers up to the square of num
        """
        total = sum((x for x in range(0, num**2)))
        return total

calculate_something(10)
calculate_something(1000)
calculate_something(10000)
