"""
    Assignment 2 - URL fetcher and parsing HTML for "dangerous" words
    ---
    Requirements:
    - Test if byte data from URL is UTF-8 decodable.
    If not, ask for a destination and save the file normally
    - Check the URLs' text data for any of the following dangerous words:
    [
        bomb, kill, terror,
        terrorist, terrorists, terrorism
    ]
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
import re
from mypackages import parsehtml
from mypackages.termcolors import color_text
from mypackages.handleurldata import get_url, validate_url, validate_response

FILE_TYPE_RE = re.compile(r"\.\w+$", re.IGNORECASE)


def validate_path(path, data_format=".html") -> str:
    """ Validate the path that the user gave """
    if len(path) < 1:
        return ""
    if not re.search(FILE_TYPE_RE, path):
        path += data_format.lower()
    return path


def save_to_file(path: str, data: bytes) -> None:
    """Save non UTF-8 byte data into a file in the given path"""
    try:
        with open(path, "wb") as file:
            file.write(data)
    except OSError as error:
        print(color_text("OSError occurred during saving:", "red"), error)
        return
    print("Succesfully downloaded:", color_text(path, "green"))


def save_to_utf(path: str, data) -> None:
    try:
        with open(path, "w") as file:
            file.write(data)
    except OSError as error:
        print(color_text("OSError occurred during saving:", "red"), error)
        return
    print("Succesfully downloaded", color_text(path, "green"))


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

    # if the data was HTML code
    if decoded_data:
        # parse HTML to text
        print("valid UTF-8")
        # count the bad words on the site
        bad_words_count = parsehtml.parse_html(decoded_data)
        print("Number of bad words found:", bad_words_count)
        path: str = input("Select a valid path and name to save file to: ")
        validate_path(path)
        save_to_utf(path, decoded_data)

    else:
        # if the url was non-HTML byte data
        print("not valid UTF-8")
        # get the filetype at the end of the url
        data_format: str = re.search(FILE_TYPE_RE, url).group()
        # select path to save file to
        path = input(
            "Select a valid path and name for the file to be saved at: ")
        if not validate_path(path, data_format):
            print("No valid path given, quitting program")
            return
        save_to_file(path, fetch_data)


if __name__ == "__main__":
    main()
