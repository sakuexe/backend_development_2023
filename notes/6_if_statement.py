"""
    If statement, Ternary Operator and User Input in Python
    ---
    Ternary operator means short inline if-else.
    Python uses the PEP 8 Style Guide
    You can use comment strings on top of any module
    to create a documentation for the module (just like this)
    ---
    Additional Information:
    - Python tutorial #4 More control flow tools
    https://docs.python.org/3/tutorial/controlflow.html
    - Flow control in python
    https://www.math.purdue.edu/~bradfor3/ProgrammingFundamentals/Python/FlowControl/
"""

# Input and Output
user_choice: str = input("Give me a number")
# print("I'm an output", sep= " ", end="\n", file=sys.stdout, flush=False)
print("automatic newline")
print("no newline", end="")
print(2,3, sep=" and ") # "2 and 3"

# Ternary operator
x = float(input("Give me a number again"))
# nice and shorthand version of writing small ifs
abs_x = x if x >= 0 else -x
# same as:
if x >= 0:
    abs_x = x
else:
    abs_x = -x

# Example
s = input("Give me a valid string: ")
if isinstance(s, str) and len(s) >= 0 and not " " in s:
    # verifying that s is a strong of not empty
    # value and that it doesn't contain any space
    print("string is valid")
# consider making it a function instead
# this will make it more readable and reusable
def valid_string(s):
    return isinstance(s, str) and \
    len(s) > 0 and not " " in s
if valid_string(s):
    print("string is valid")
