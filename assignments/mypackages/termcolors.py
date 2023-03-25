import os

tcolors = {
    "cyan": "\033[96m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "gray": "\033[90m",
    "clear": "\033[0m",
    "underline": "\033[4m",
    "bold": "\033[1m",
}

def color_text(string: str, color: str) -> str:
    """ Changes the given string's color and returns it """
    color = tcolors[color]
    return f"{color}{string}{tcolors['clear']}"

def clear() -> None:
    """ Clear terminal based on if the user's OS is unix or DOS based """
    _ = os.system('clear' if os.name == 'posix' else 'cls')
