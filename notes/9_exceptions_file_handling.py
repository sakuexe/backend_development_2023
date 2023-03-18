"""
    * 9 - Exceptions and File Handling in Python
    ---
    Even if a statement or expression is syntatically correct,
    it may cause an error when an attmept is made to execute it.
    Errors detected during execution are called exceptions.
    For example:
    - IndexError - index out of range
    - NameError - name not defined
    - OSError - operating system related error e.g. error accessing a file
    - SyntaxError - erroneus syntax
    - TypeError - cannot concate different types
    - ValueError - invalid type
    - ZeroDivisionError - division by zero
    ---
    Additional information
    - Python Exceptions: an Introduction:
    https://realpython.com/python-exceptions/
    - Reading and Writing Files in Python:
    https://realpython.com/read-write-files-python/
    - Working with Files in Python:
    https://realpython.com/working-with-files-in-python/
"""

# Syntax for try except
# and it's all possible blocks
try:
    pass
# Handle this error
except NameError:
    pass
# handle another error
except ValueError:
    pass
# else gets run after the try block is run without errors
else:
    pass
# finally is done after everything is done. Errors or not
finally:
    pass

# Although only try/except is required
try:
    pass
except NameError:
    pass

# You can also use except:
# but it is NOT recommended, it does catch Any exceptions
try:
    pass
except:
    pass

# Example
from functools import lru_cache
import sys
try:
    with open("testfile.txt", "r") as f:
        s = f.readline()
        i = int(s.strip())
        print(i)
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data into an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# Another example
# command line arguments
# the first argument is the name of the file
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
            print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        # file has n lines
        f.close()

# Handling files
# Read the whole external file
# Basic pattern is as follows:
# b = binary mode - used for audio/video/image files
# open file mode = "r/w/a/rb/wb/ab/r+/rb+/w+/wb+/a+/ab+"
# f = open("filepath", "mode")
# do your file processing d = f.read(); f.write(d)
# f.close()  # closing a file starts to flush the results

# But the following is better
# with open("testfile.txt", "mode") as f:
    # process file
    # file is closed automatically by python

# Reading a file - All at a time
with open("testfile.txt", encoding="utf-8") as f:
    print(f.read())

# Read line by line
with open("testfile.txt") as f:
    for line in f:
        print(line.rstrip())

# Reading a file, line at a time and print with line numbers
with open("testfile.txt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, start=1):
        print(i, line.rstrip())

# Write to external file (Creates a new file if doesn't exist)
# encoding is not required but is recommended
with open("testfile.txt", "w", encoding="utf-8") as my_file:
    my_file.write("Eka rivi \n")
    my_file.write("Toka rivi \n")
    # Flush removes the allocated memory from RAM
    # moves it to disk
    print("可疑的", file=my_file, flush=True)
    # alternatively you can use the following for flushing:
    my_file.flush()

# Append data to the end of file:
with open("test.txt", "a") as my_file:
    my_file.write("One more line\n")
# Append data to the beginning of the file:
with open("test.txt", "r+") as file:
    old = file.read()
    file.seek(0, 0)  # seek to start of file
    file.write("New line to start with\n")
    file.write(old)  # write old contents of file

# Reading and copying data from URLs
# Reading data over HTTP from URLs work just like files.
# Note that returned data is always binary (bytes)
from urllib.request import urlopen
url = "https://yle.fi/uutiset"
with urlopen(url) as response:
    data = response.read().decode("utf-8")
    print(data[:1001])  # display only first 1000 characters

# use cache easily with the following decorator
# @lru_cache(maxsize=64)

# .strip() removes whitespaces from both sides
"   Sus    ".strip()
# .rstrip() removes whitespaces from only right side
"   Sus    ".rstrip()

# Using JSON in Python
import json
d = {"name": "example", "number": 123, "list": [1,2,3]}
obj = json.dumps(d)
print(obj)
s = json.loads(obj)

with open("mydata.json", "w") as f:
    json.dump(d,f)
    print("json data saved")

with open("mydata.json", "r") as f:
    obj = json.load(f)
    print(obj)

# Serialization using Pickle
# The pickle module implements binary protocols for serializing
# and deserializing a python object structure
# Pickling is the process whereby a Python object hierarchy
# is converted into a byte stream, and unpickling is the inverse
import pickle
d = {"name": "exampleÄÖÅ", "number": 123, "list": [1,2,3]}
with open("mydata.pickle", "wb") as f:
    obj = pickle.dump(d, f)

with open("mydata.pickle", "rb") as f:
    obj = pickle.load(f)
    print(obj)
