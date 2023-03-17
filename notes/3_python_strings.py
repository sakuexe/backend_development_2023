"""
    * 3 - Python Strings
    ---
    Useful Links:
    - Python tutorial 3 - an informal introduction to python
    https://docs.python.org/3/tutorial/introduction.html
    - Python String Methods
    https://docs.python.org/3/library/stdtypes.html#string-methods
    - TutorialsPoint - Python Strings
    https://www.tutorialspoint.com/python/python_strings.htm
"""

# Single and double quotes are interchangeable and can be mixed
example_string: str = "This is a string"
example_string += ', and this is too' # "This is a string, and this is too"

# Raw strings make it easier to write regular expressions
two_numbers = r'\d\d'
biden = r"Joe \"Sleepy\" Biden"

# Using three quotes makes it easy to write multi-line string literals
documentation_string = """Line #1
    Line #2
    The end"""
print(documentation_string)

# String is immutable sequence type, meaning it's value cannot be changed
# after creation. So create a new variable for the changed string instead

simpson = "Bart Simpson"
# a[0] = f - Would not work
"""
    [start, end (not included), steps]
    an empty spot uses defaults [0:-1:1]
    simpson[:4] == "Bart"
    simpson[::2] == "Br Smsn"
"""
reverse_simpson = simpson[::-1]

# String methods
print(simpson.count("s")) # 2
# return an encoded version of the string
simpson.encode(encoding="utf-8", errors="strict")
# returns a new string in lowercase
lower_simpson = simpson.lower()
# replace old with new
lower_simpson.replace("S", "Ch")
# split onto a new list of characters
simpson_list = simpson.split()

# String formatting ways
# Old syntax - C inspired
test = "Value of %s is %.3f" % ("xyz", 2.4244242)
# a bit less old syntax - Python 2.6
test2 = "Value of {0} is {1:.2f}".format("PI", 3.14159)
# f strings - Python 3.6+
name = "Pi"
value = 3.14159
print(f"Value of {name.upper()} is {value:.3f}")
# You can use vars() to fetch the variables currently in use
old_and_cool = "Value of %(name) is %(value).3f" % vars()

b = simpson.encode("utf-8")
decoded = b.decode("utf-8")

# iterate through words one at a time
web_string = "Web programming is my favorite"
for word in web_string.split(): print(word)

# Remove whitespaces from the start and end of string
strippable = "    what is going on    "
stripped = strippable.strip()
stripped_start = strippable.lstrip()
stripped_end = strippable.rstrip()

phone_input = "  +358 044 243 5742    "
phone = phone_input.replace(" ", "")
print(phone) # +3580442435742

# check if a file is a valid picture format
file_paths = ["pic.jpg", "text.txt", "logo.png"]
file_endings = (".png", ".gif", ".jpg", ".jpeg")
for path in file_paths:
    if path.endswith(file_endings):
        print(path)
