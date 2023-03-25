import json
from typing import Dict
from mypackages.termcolors import color_text, clear

# save the type hint for dictionary - for conciseness
word_dict = Dict[str, str]


def save_to_json(filename: str, dictionary: word_dict) -> None:
    """ Save the current Words-dictionary to a file with 
        the given filename and path
    """
    try:
        with open(filename, "w") as file:
            jsoned = json.dumps(dictionary)
            file.write(jsoned)

    # if file cannot be written, due to permissions or similar
    except OSError as error:
        print(color_text("Error saving file:", "red"), error)
        # guard clause return
        return

    # if file cannot be written, due to permissions or similar
    except MemoryError as error:
        print(color_text("Memory is full, cannot save file:", "red"), error)
        # guard clause return
        return

    # if the file is corrupted, or JSON is wrong syntax
    except TypeError as error:
        print(color_text("Couldn't save JSON:", "red"), error)
        # guard clause return
        return

    # If no errors occur
    print("Succesfully saved dictionary to:", color_text(filename, "cyan"))


def load_json(filename: str) -> word_dict:
    """ Load JSON data inside of a given filename """
    DEFAULT_DICT = {"cow": "lehmä", "rat": "rotta", "raccoon": "pesukarhu"}

    try:
        with open(filename, "r", encoding="UTF-8") as file:
            read_file = file.read()
            response = json.loads(read_file)
        return response

    # if file can't be read
    except OSError as error:
        print("File:", color_text(filename, "red"), "could not be read", error)
        print(
            f"Creating new file {color_text('./'+filename, 'cyan')} and initializing new dictionary\n")
        return DEFAULT_DICT

    # if JSON inside of the file was not in correct format
    except ValueError:
        print("File:", color_text(filename, "red"), "was not found")
        print(
            f"Creating new file ./{filename} and initializing new dictionary\n")
        return DEFAULT_DICT


def list_dictionary(dictionary: word_dict) -> None:
    print("-----")
    for word, desc in dictionary.items():
        print(word, "=", desc)
    print("-----")


if __name__ == "__main__":
    # initialize the dictionary by fetching the JSON file
    words: word_dict = load_json("dictionary.json")

    while True:
        length: str = str(len(words))
        print(
            f"Current number of items in dictionary: {color_text(length, 'cyan')}")
        print(
            f"Press {color_text('enter', 'cyan')} or input '{color_text('q!', 'cyan')}' to quit the program")
        print(f"View the dictionary by inputting '{color_text('ls', 'cyan')}'")
        new_word = input("Search for a word in dictionary: ").lower()
        # if input is enter or q! To quit program
        if not new_word or new_word == "q!":
            break
        if new_word == 'ls' or new_word == 'list':
            list_dictionary(words)
            continue
        if new_word in words:
            print("-----")
            print(new_word, "=", words[new_word])
            print("-----")
            clear()  # clear the terminal to avoid cluttering
            continue
        # if given word is not found
        not_found = f"{color_text(new_word.upper(), 'cyan')} was not found in the dictionary. \n" + \
            "Give a definition for the word or press enter to search again. \n" + \
            "Definition: "
        definition = input(not_found).lower()
        if not definition:
            clear()  # clear the terminal to avoid cluttering
            continue
        words[new_word] = definition
        print(f"Added {new_word} to dictionary!")

        clear()  # clear the terminal to avoid cluttering

    # When the program stops running, save the words dictionary into dictionary.json
    print("-----")
    save_to_json("dictionary.json", words)
