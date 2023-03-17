"""
    4 - Sequence Types in Python
    List, Tuple, Set and Deque
    ---
    Additional information
    - Python Sequence Types
    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
    - Python like you mean it - Sequence Types
    https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/SequenceTypes.html
"""

# Lists in python are mutable
zeroes: list = [0]*100 # List with 100 zeros

# find smallest, largest and the sum of an array
numbers = [x for x in range(1, 11)]
print(min(numbers)) # 1
print(max(numbers)) # 10
print(sum(numbers)) # 55

# Example use case of min() and max()
X_MAX = 200
x = 100
increment = 60
# return the smaller of the two parameters
x = min(x + increment, X_MAX)
# you could do the same in reverse with max()
# returns the bigger parameter of the two
x = max(x + increment, X_MAX)

# Turn a list into a string
names: list = ["Maya", "Hee", "Sam", "Michael", "Pedro", "Carlos"]
# " " is the string that gets placed in between the list elements
names_converted: str = " ".join(names) 
# Make a string into a list
names_remade = names_converted.split()

# Tuples
# Tuples are basically immutable lists
ones: tuple = (1, 1, 1, 1, 1, 1)
# ones[-1] = 2 - Doesn't work, since touple can't be changed

# Slicing
# list[start : end : stepping]
testing: list = list(range(10))
# print out the first 5 elements with 2 steps at a time
print(testing[:6:2]) # 0, 2, 4
testing = testing[::-1] # 9, 8 ,7 ...

# Reverse a list
reversed = testing.reverse()
# A more efficent way of reversing a list
reversed = testing.sort(reverse=True)

# Copy by reference vs Shallow copy
a = list(range(100))
# make a shallow copy, so that you won't change the original
b = a.copy()
# or you can copy with slicing
b = a[:]
b = b[:10]
print(a, b) # [1,2,3,4 ... 99], [1,2,3, ... 9]

# Sets
# Sets are like lists, where you can't have multiple elements with the same value
# So it will remove duplicates
example: set = set(list(range(15))) # { 1, 2, 3, ... 14 }
# Union - add two sets together
a = {1,2,3,4,5}
b = {10,8,6,4}
c = a.union(b)
print(c)

# Deque
# Deque is a container datatype that allows you to get the first and last values
# of the list in O(1) time, compared to list, which has a time complexity of O(n)
# a.popleft() - allows you to get the last element of a deque and remove it
# a.appendleft() - allows you to append to an element to the start of the deque
# ---
# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque
from timeit import timeit

print("Deque Documentation:")
print(deque.__doc__)

def list_test(n):
    a = []
    for i in range(n):
        a.insert(0, i)
    return a

def deque_test(n):
    a = deque([])
    for i in range(n):
        a.insert(0, i)
    return a

if __name__ == "__main__":
    print("List:", timeit("list_test(10**5)", setup="from __main__ import list_test", number=10))
    # List: 15s
    print("Deque:", timeit("deque_test(10**5)", setup="from __main__ import deque_test", number=10))
    # Deque: 0.071s
