"""
    Loops in Python
    ---
    While, For, Reverse Loops, Nested Loops, break and continue
    ---
    Additional information:
    - Loops in Python
    https://www.geeksforgeeks.org/loops-in-python/
"""

# While loop
x = 1
while x <= 10:
    print(x)
    x += 1
# while loops can have an optional else statement at the end
# IF NO breaks are encountered
else:
    print("ended normally")
print("yeah, what the optional else said")
# Reverse while loop
while x >= 1:
    print(x)
    # The steps amount
    x -= 1
print("end2 - the endening")

# Python does not have Do While
# but we can emulate it with the following
x = 1
while True:
    print(x)
    x += 1
    # check the condition at the end of loop
    # instead of at the start
    if x>10: break

# For loop
# the way range works is range(start, end, steps)
for i in range(0, 31, 3):
    print(i)
# for loop, just like while can have an optional
# else condition at the end of the loop
# but only IF NO breaks occur
else:
    print("Ended normally")
print("Yeah")
# Reverse for loop
for i in range(10, 0, -1):
    print(i)

# Iterate through lists with for loop
names = ["Charles", "Max", "Carlos", "Lewis", "Kimi", "Valtteri", "Niki"]
for index, name in enumerate(names):
    print(index, "-", name)

animals = {"Cat": "Kissa", "Dog": "Koira", "Monkey": "Apina", "Rat": "Rotta"}
# iterate through a dictionary and access it's key and value
for english, finnish in animals.items():
    print(english, "=", finnish)
# access only the values
for value in animals.values():
    print(value)
# access only the keys
for value in animals.keys():
    print(value)

# Reverse a for loop
for name in reversed(names):
    print(name)
# This also works, but don't do this!
# it slices and creates a new data structure before iterating through it
for name in names[::-1]:
    print(name)
# This also works, but is unreadable
for x in range(100, -1, -1):
    print(x)

# Nested loops
# Multiplication table done with nested loops
N = 10
for y in range(1, N+1):
    for x in range(1, N+1):
        # %4d adds 4 character padding
        print("%4d " % (x*y), end="")
    print()

# Break and Continue
# break exits from for or while loop
# continue continues the nearest cycle of for or while loop (goes to beginning of loop)
numbers = []
while True:
    s = input("Positive integer? (enter to quit): ")
    if not s:  # almost the same as if len(s) == 0
        break
    if not s.isdigit():
        continue  # go to beginning
    i = int(s)
    if i >= 0:
        numbers.append(i)
print("Numbers:", numbers)
print("The sum of the given numbers is:", sum(numbers))
