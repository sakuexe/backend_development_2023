from html.parser import HTMLParser
import re
from mypackages.mydecorators import timeit

# Choose which tags to completely remove from the parsing
# I chose style, head and script, since they cannot be read on the page
# by normal users
REMOVED_TAGS = ["style", "head", "script"]
BAD_WORDS = [
    "bomb", "kill", "murder", "terror", 
    "terrorist", "terrorists", "terrorism"
]

class WordWarning(HTMLParser):
    """ Custom HTML Parser for counting words from a HTML file.
        \n
        This parser stores the parsed text into a string variable.
        This string variable can be returned easily for debugging,
        or further analyzing.
        \n
        For this assignment though, only the "matches" counter is used.
    """
    parsed_text: str = ""
    _matches: int = 0

    def handle_data(self, data: str) -> None:
        """ Handles data by removing unwanted HTML code and then finding
            matches for dangerous words.
            \n
            Also stores the filtered data onto a Deque, for easy debugging.
        """
        inner_text = self.filter_html(data)
        if inner_text != " ":
            self.parsed_text += inner_text.strip() + "\n"

    def filter_html(self, raw_html: str) -> str:
        """ For actually removing the HTML code from the string data """
        # first remove all tags and their inner attributes
        filtered = re.sub(r'<.*?>', '', raw_html)
        # then remove all newlines and tabs, replace with one space
        filtered = re.sub(r'[(\n)(\t)]{1,}', ' ', filtered)
        return filtered

    @timeit
    def find_all_matches_string(self) -> int:
        """ Find all matches for bad words in the parsed text. """
        for word in BAD_WORDS:
            matches = re.findall(f"\\b{word}\\b", self.parsed_text, re.I)
            self._matches += len(matches)
        return self._matches

def parse_html(data: str) -> int:
    parser = WordWarning()
    # remove all the unwanted tags from REMOVED_TAGS
    for tag in REMOVED_TAGS:
        data = re.sub(r'<'+tag+r'.*?>(.|\n)*?</'+tag+r'>', '', data)
    parser.feed(data)
    # return the number of matches of bad words
    return parser.find_all_matches_string()
    # return parser.parsed_text
