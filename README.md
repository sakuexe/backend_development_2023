# **Backend Web Development - 2023**

_By Saku Karttunen_

### About

This repository includes exercises, assignments and notes from
HAMK Riihimäki's "Backend Web Development" -course

- Teacher and course organizer: **Petri Kuittinen**
- Course duration: **13.3. - XX.4.2023**
- Editors used: **Neovim**
- Languages & Frameworks used: **Python & Django**

## Assignments

Lorem ipsum dolor sit amet, qui minim labore adipisicing minim
sint cillum sint consectetur cupidatat.

1. **Python dictionary and JSON**

Make a simple dictionary application, which can save the dictionary 
in JSON format. The user can search words from the dictionary. 
If the word is found, it displays the translation. if the word is not found, 
the program displays "Word not found. Please input a definition". 
If user submits a definition, it adds a new word to this dictionary. 
There should be a way to exit the application e.g. input an empty string.

When the application is started it checks if the file containing the dictionary 
exists and will try to load the dictionary. If loading fails, it starts with 
an inbuilt default dictionary, which might contain just few words. 
The application must save the dictionary, including newly added words, 
when the user exits the application. The program should behave well 
and display according error message even when errors occur e.g. it is not possible 
to save the dictionary or load it.

2. **URL fetcher and parsing HTML for "dangerous" words**

Make a program, which will ask the user for a valid URL to download. 
Then the program tries to load the contents of the URL into memory.

It if contents look like a HTML file with utf-8 encoding, it tries to 
HTML parse it and check if the content has some dangerous words. 
The content is the content, which is not part of HTML tags, meaning 
the text part of the web page. The dangerous words are: "bomb", "kill", 
"murder", "terror", "terrorist", "terrorists" and "terrorism". 
Note that these should be treated as separate words. In other words "bomba", 
"killer" or "antiterrorism" are not dangerous words. The check should ignore 
the case e.g. "bomb", "BoMb" or "BOMB" are all dangerous words.

The program should display the amount of dangerous words found from the web page. 
If the contents don't use utf-8 encoding, e.g. it is binary file, like image, 
it can ignore this part. You do not need to actually validate the HTML

Finally the program asks the user for a path where to save the contents. 
This should allow the user to save both binary files (audio, images, video) 
and text files (HMTL, CSS, JavaScript) to the local file system.

The program should not crash, but display according error mistakes if 
something goes wrong e.g. the URL is malformed or cannot be loaded or 
the file cannot be saved.

3. **Complete the Django Tutorial and migrating to MySQL**

Complete the entire official Django tutorial (parts 1-7). There is a series of videos,
which will go through all of these found among the quiz questions.

Besides the official Django Tutorial, you must copy data from Sqlite3 database and migrate
things to MySQL database. You need to install MySQL and required software.

By default, Django uses SQLite3 as the database engine. Take a backup of your data to JSON format. 
Take a complete backup to a file named all.json and partial backup, which only has the polls 
application data into a file called polls.json. Change the database to use MySQL. 
Migrate the polls data from the SQLite database to MySQL. And you probably need to 
make a new superuser password when you create a new database with MySQL. 
Loading all data to MySQL will probably fail because of duplicate keys, 
but copying just polls data should work.

## Useful links

- [Python Standard Library Docs](https://docs.python.org/3/library/)
- [Microsoft Azure Portal](https://portal.azure.com/)
- [WinSCP](https://winscp.net/eng/index.php)
- [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)
