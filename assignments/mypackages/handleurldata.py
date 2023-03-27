"""
    Functions for 2_url_fetcher.py
    ---
    split into seperate files for easier reading
"""
from urllib import request
from urllib.error import URLError
import re


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


def validate_response(response) -> str:
    """ Validate the byte data gotten from a URL
        If it cannot be decoded to UTF-8, return False boolean"""
    try:
        return response.decode("utf-8")
    except UnicodeError as error:
        print("Given link does not contain UTF-8 data")
        return ""
    except ValueError as error:
        print("Decoding link error:", error)
        return ""
