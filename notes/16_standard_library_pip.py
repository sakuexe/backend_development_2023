"""
    Python Standard Library and PIP
    ---
    Additional Information
    - What is PIP - A guide to new pythonistas
    https://realpython.com/what-is-pip/
    - IPython Tutorial
    https://ipython.readthedocs.io/en/stable/interactive/tutorial.html
    - IPython Built-In Magic Commands
    https://ipython.readthedocs.io/en/stable/interactive/magics.html
"""

import math
X = 1234.5678
print("X rounded:", round(X))
print("X rounded down:", math.floor(X))
print("X rounded up:", math.ceil(X))
print("10 base logarithm of 2 is:", math.log10(2))
print("Square root of 2 is:", math.sqrt(2))
print("e to the power of 2 is", math.exp(2))
print("sin(0)", math.sin(0))
print("cos(0)", math.cos(0))
print("tan(0)", math.tan(0))
print("180 degrees in radians is", math.radians(180))
print("PI in degrees is", math.degrees(math.pi))

# Easy way to convert binary to integers
print(int("00101", base=2))  # 4

import random
print(random.random())  # random float between 0.0 - 1.0
print(random.randrange(1,7))  # random int between 1..6
print(random.randint(1,6))  # random int between 1..6
print(random.choice(["yes","no","maybe"]))  # random choice
a = list(range(1, 101))
random.shuffle(a)  # randomize the order of given list
print(a[:10])
lottery = random.sample(range(1,41), 7)
print(sorted(lottery))

# Statistics
from statistics import mean, median, mode
a = [1, 0, 3, 2, 2, 10, 5, 4, 3, 2, 6, 7]
print("Average:", mean(a))  # 3.75
print("Median:", median(a))  # 3.0
print("Most common", mode(a))  # 2

# Datetime module
import datetime
birth = datetime.date(1990, 12, 31)
now = datetime.date.today()
print(f"{now.day}.{now.month}.{now.year}")
print(now.strftime("%d.%m.%Y. Month is %B."))
delta = now-birth
print(delta)
week_in_future = now + datetime.timedelta(days=7)
delta2 = week_in_future - now
print(delta2.days)

# OS module
import os
print("current working directory", os.getcwd())
os.chdir("/tmp")  # change current working directory
# run system commands, which can be very risky!
os.system("mkdir example123")  # can run ANY command
print(os.system("ls -la"))
print("passwd size", os.lstat("/etc/passwd").st_size)
os.system("rmdir example123")
print("HOME", os.environ["HOME"])
print("PATH", os.environ["PATH"])
f = open("test.txt", "w")
f.write("One\n")  # starts to write to internal buffer
os.fsync(f.fileno())  # force changes to disk
f.close()
os.unlink("/tmp/test.txt")  # remove file

# SYS module
import sys
print("Python version:", sys.version)
print("Python path", sys.path)
print("Platform:", sys.platform)
print("Command line arguments:")
for arg in sys.argv[1:]:
    print(arg)
print("Standard error", file=sys.stderr)
# same as print(input(""))
# with sys.stdin as f:
#     d = f.readline()
#     print(d)
# sys.exit(0)

# Enumerations
from enum import Enum, auto
class IceCream(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    STRAWBERRY = 3
    MINT = 4

for icecream in IceCream:
    print(icecream)

class Suits(Enum):
    hearts = auto()
    spades = auto()
    clubs = auto()
    diamonds = auto()

for suit in Suits:
    print(suit)

# SQLite3 module
# SQLite comes inbuilt with Python
# Good enough for testing and small usage
import sqlite3
# ":memory" for memory only
conn = sqlite3.connect("mydatabase.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS persons (id int, name text) ")
c.execute("insert into persons values(1, 'Jack')")
c.execute("insert into persons values(2, 'Jill')")
c.execute("insert into persons values(3, 'Bob')")
conn.commit()
for id, name in c.execute("select * from persons"):
    print(id, name)

c.execute("drop table persons")  # clean up
conn.commit()
conn.close()

# Timing things
from timeit import Timer
# manually construct a list of squares
print(Timer("a=[];\nfor x in range(1,100001): a.append(x*x)").timeit(number=5))
# use list comprehension
print(Timer("[x*x for x in range(1,100001)]").timeit(number=5))
# use generators
print(Timer("list(x*x for x in range(1,100001))").timeit(number=5))
# Mulitply x by 32
print(Timer("x=13;x*32").timeit())
# Shift x 5 bits left, same as * 32
print(Timer("x=13;x<<5").timeit())

# HTML Parser module
from html.parser import HTMLParser
from urllib.request import urlopen

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            for attr, value in attrs:
                if attr=="href":
                    print("link:", value)
    # def handle_endtag(self, tag: str) -> None:
    #     pass
    # def handle_data(self, data: str) -> None:
    #     pass

parser = MyHTMLParser()
with urlopen("https://yle.fi/uutiset") as f:
    data = f.read()
    parser.feed(data.decode("utf-8"))

# Least Recently Used (LRU) Cache module
from functools import lru_cache
from urllib.request import urlopen, HTTPError

# lru cache allows storing latest data to RAM memory
# it does it automatically and when max size is over given value
# it removes the oldest data
# how cool and easy is that??
@lru_cache(maxsize=64)
def get_pep(num):
    """Retrieve text of a Python Enhancement Proposal"""
    resource = f"http://www.python.org/dev/peps/pep-{num}"
    try:
        with urlopen(resource) as s:
            return s.read().decode("utf-8")
    except HTTPError:
        return "Not Found"

while True:
    s = input("Give PEP number?")
    if not s: break
    if not s.isdigit(): continue
    n = int(s)
    pep = get_pep(n)
    i = pep.find("PEP ")
    j = pep.find(" |", i)
    print(n, len(pep), pep[i:j])

print(get_pep.cache_info())

# Pip (Python package manager)
# update pip with the following:
# pip3 install -U pip  - Linux
# python -m pip install -U pip  - Windows
# update packages with the same command
# but just replace the last "pip" with the package
