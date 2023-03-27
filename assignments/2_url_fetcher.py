"""
    Assignment 2 - URL fetcher and parsing HTML for "dangerous" words
    ---
    Requirements:
    - Test if byte data from URL is UTF-8 decodable.
    If not, ask for a destination and save the file normally
    - Check the URLs' text data for any of the following dangerous words:
        * bomb
        * kill
        * terror
        * terrorist
        * terrorists
        * terrorism
    - The words above need to be separate.
    (So no matches for words like bomba, killer or antiterrorism)
    - The words need to be case insensitive
    - save the contents of the file onto a local file
    - Give an error message and stop (and not crash) the program
    - Ask the user for the path of which to save the file into
    ---
    Use the command "pip3 install -r requirements.txt"
    to install all the needed pip packages for these assignments
"""
from urllib import request
from urllib.error import URLError
import os
import re
from mypackages import parsehtml
from typing import Union

def get_url(url: str) -> bytes:
    """Get the raw byte data of a given URL"""
    try:
        with request.urlopen(url) as file:
            response = file.read()
        return response
    except ValueError as error:
        print("Invalid URL:", error)
        return bytes()
    # if URL passes value error but is still invalid
    except URLError as error:
        print("Invalid URL:", error)
        return bytes()
    # URLError is a subclass of OSError, so catch other OSErrors
    except OSError as error:
        print("Unexpected OSError:", error)
        return bytes()

def validate_url(url: str) -> str:
    """ Check if the URL starts with "https://" or "http://".
        If not, lets add https:// to the start"""
    if not re.match(r"^http(s)?://", url):
        print("Adding https:// to the front of URL")
        return "https://" + url
    print("URL valid")
    return url

def validate_response(response) -> Union[str, bool]:
    """ Validate the byte data gotten from a URL
        If it cannot be decoded to UTF-8, return False boolean"""
    try:
        return response.decode("utf-8")
    except UnicodeError as error:
        print("Given link does not contain UTF-8 data")
        return False
    except ValueError as error:
        print("Decoding link error:", error)
        return False

def save_to_file(path: str, data: bytes) -> None:
    """Save non UTF-8 byte data into a file in the given path"""
    try:
        with open(path+"-temp", "wb") as file:
            file.write(data)
        # change the name of the downloaded file to include the format
        file_format = ""
        os.rename(f"./{path}-temp", f"{path}.{str(file_format).lower()}")
    except OSError as error:
        print("OSError:", error)

def save_to_utf(path: str, data) -> None:
    with open(path, "w") as file:
        # for line in data:
        #     file.write(line+"\n")
        file.write(data)

def main() -> None:
    # Get the URL
    url = input("Give me a valid URL: ")
    url = validate_url(url)
    # Download and check URL
    fetch_data = get_url(url)
    if not fetch_data:
        # If URL was not a valid one, exit program
        return

    decoded_data = validate_response(fetch_data)
    if decoded_data:
        # parse HTML to text
        # Generator vs All at once?
        print("valid UTF-8")
        # count the bad words on the site
        bad_words_count = parsehtml.parse_html(decoded_data)
        print("Number of bad words found:", bad_words_count)
        save_to_utf("testinggggg.txt", decoded_data)
    else:
        print("not valid UTF-8")
        # select path to save file to
        path = input("Select a valid path for the file to be saved at: ")
        save_to_file(path, fetch_data)

if __name__ == "__main__":
    main()
