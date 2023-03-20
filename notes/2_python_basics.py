"""
    * 2 - Python Basics
    ---
    Read more about this:
    Official python tutorial - highly recommended
    https://docs.python.org/3/tutorial/
    Official python documentation - besides the tutorial, the library reference is essential
    https://docs.python.org/3/
    LearnPython - a free interacitive tutorial, great for self learning
    https://www.learnpython.org/
    FreeCodeCamp - free interacitive materials, especially for python
    https://www.freecodecamp.org/learn
    Python Cheatsheet - for those who are in a hurry
    https://www.pythoncheatsheet.org/
""" 

# Python Names
characters_to_use = (
    "A-Z",
    "a-z",
    0-9,
    "_"
)
# Class names should be capitalized
class ClassName:
    print("")
class Matrix:
    print("")
# Constants
CONSTANT_VARS = "Written in uppercase"
# Use descriptive names
descriptive_variable = True

# How to download a files online with python
from urllib.request import urlopen
with urlopen("https://docs.python.org/3/library/index.html") as html:
    read_html = html.read()
    decoded_html = read_html.decode("utf-8")
    # print the first 1000 characters
    # print(decoded_html[:1000])

picture = urlopen("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b9e405d8-7e26-4ce3-a7d8-dd388ca2b4dc/d5n7ux4-805504ea-a62b-4805-a8f3-43d519978ee2.png/v1/fill/w_1024,h_747,strp/png__rat_2_by_moonglowlilly_d5n7ux4-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzQ3IiwicGF0aCI6IlwvZlwvYjllNDA1ZDgtN2UyNi00Y2UzLWE3ZDgtZGQzODhjYTJiNGRjXC9kNW43dXg0LTgwNTUwNGVhLWE2MmItNDgwNS1hOGYzLTQzZDUxOTk3OGVlMi5wbmciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.AHE3DcOVDMOi5rdqYv-2HdsdVZ_L5NxDmfM_0feobC0")
read_picture = picture.read()
# print(len(read_picture))
picture = open("ratmode.png", "wb")
picture.write(read_picture)
picture.close()

# You can remove the dynamic nature of variables with static typing
just_a_string: str = "Can't make me into an int"
# just_a_string = 2 - This will give an error
# but this will work
just_a_string = "This I am fine with"
