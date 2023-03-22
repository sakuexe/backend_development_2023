"""
    Regular Expressions in Python
    ---
    Test your regexes easily in the browser here:
    https://www.regextester.com/
    ---
    Additional Information
    - Python Regular Expression (re) module
    https://docs.python.org/3/library/re.html
    - Regular Expression HOWTO
    https://docs.python.org/3/howto/regex.html
    - Regular Expressions: Regexes in Python (Part 1)
    https://realpython.com/regex-python/
    - Regular Expressions: Regexes in Python (Part 2)
    https://realpython.com/regex-python-part-2/
"""

# import with re, part of standard library
import re

string: str = "testing 0213"

# scan the string to find first match
re.search(r"\w", string, flags=0)

# match from beginnning of string
re.match(r"\w", string, flags=0)

# Match entire string
# kinda like ^ and $
re.fullmatch(r"\w", string, flags=0)

# split string by occurences of string into list of string
re.split(r"\w", string, flags=0)

# return all non-overlapping matches of pattern in a string as a list of strings
re.findall(r"\w", string, flags=0)

# replace all non-overlapping occurences of pattern in string with replaced variable
replaced: str = "no_numbers"
re.sub(r"\d", replaced, string, count=0, flags=0)

# Search() searches for the first match inside the string
# no matter where the match is found at
m = re.search(r"\d{5}", "Zip code is: 12345")
# match() looks for the match starting from the very first index forwards
m = re.match(r"^\d{5}", "123456")
# removes the need for ^ and $
m = re.fullmatch(r"\d{5}", "12345")

print(m)
print(re.findall(r"\d{5}", "zip codes: 11100, 11130 and 00200"))
numbers = re.split(r", ", "1, 2, 100, -5")
print(", ".join(numbers))
print(re.sub(r"\d{5}", "xxxxx", "Censored: 12345 and 00200"))

words = "apple,banana, fruit"
print(words.split(","))  # "apple", "banana", " fruit"
print(re.split(r",\s*", words))  # "apple", "banana", "fruit"

words = """
    python, javascript, C#, Swift
    apple,fruit,banana,mango, orange
    blue,red,white, black
"""

lines = words.splitlines()
print(lines)
reformatted = [word for line in words.splitlines() for word in re.split(r",\s*", line)]
print(" ".join(reformatted))

# Validate if input is an integer between 1 - 100
user_number = input("Give me integer between 1 - 100: ")
if re.match(r"^(100|[1-9]d?)$", user_number):
    print("Correct")
else:
    print("Incorrect")

information = "Procuct 1, price: 50 €, weight: 40 g. Product 2, price: 25 €, weight: 120 g"
# get all of the weights and sum them together
weights = re.findall(r"(\d+) g", information)
weights = [int(weight) for weight in weights]
print(weights)
print("Sum of weights:", sum(weights))

# get all of the prices and censor them
censored = re.sub(r"(\d+) €", "XXX", information)
print(censored)

# Pre-Compiling Regular expressions using Groups
# This makes it more readable and easier to reuse
zip_re = re.compile(r"(\d+) g")
zip_re.findall(information)

phone_re = re.compile(r"(\d{2,4})-(\d{1,10})")
print(phone_re.match("050-1234567").groups())  # {'050', '1234567'}
print(phone_re.match("050-1234567").group(0))  # '050-1234567'
print(phone_re.match("050-1234567").group(1))  # '050'
print(phone_re.match("050-1234567").group(2))  # '1234567'

phone_re = re.compile(r"(?P<operator>\d{2,4})-(?P<number>\d{1,10})")
print(phone_re.match("050-1234567").groups())  # {'050', '1234567'}
print(phone_re.match("050-1234567").group(0))  # '050-1234567'
print(phone_re.match("050-1234567").group(1))  # '050'
print(phone_re.match("050-1234567").group("operator"))  # '050'
print(phone_re.match("050-1234567").group(2))  # '1234567'
print(phone_re.match("050-1234567").group("number"))  # '1234567'

def valid_user_name(s: str):
    """
    Use regular expression to test that user_name
    begins with character a-z and is 3 to 19 characters in length
    and only contains characters a-z 0-9
    """
    return re.fullmatch(r"[a-z][a-z\d]{2,9}", s)

user_name = input("user name?")
if valid_user_name(user_name):
    print("User name is valid")
else:
    print("Invalid user name")

# Validate floating point numbers
re_floating_number = re.compile(r"[-+]?\d*\.?\d+")
re_floating_exponent = re.compile(r"[-+]?(\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?")

number_string = "Here are some floating point numbers\
3.14 123.5423, 0.2:0.0 -5.6 +3.54 0.0001 10.0 and -2.0"

num_strings = re_floating_number.findall(number_string)
print(num_strings)

import random

def random_suffix(m):
    """
    random.choice() chooses a random element from the given list
    """
    return m.group(0)+random.choice(("Script", "Basic", "Code", "++"))
about_me = "I like to code in Java, Python and C#. And I use Visual Studio Code."
about_me = re.sub(r"Java|Python|Visual|C#|Code", random_suffix, about_me)
print(about_me)

# Use \bWORD\b to find just the WORD, not any other words that include it
re.findall(r"is", "Here is some text. This is also more text")  # len(this) = 3
re.findall(r"\bis\b", "Here is some text. This is also more text")  # len(this) = 2

# use re.I to ignore case
re.findall(r"\bbomb\b", "Here is a BOMB", re.I)
