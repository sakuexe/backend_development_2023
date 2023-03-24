import json
from typing import Dict

words: Dict  = {"Dog": "Koira", "Cat": "Kissa"}

def save_to_json(filename: str) -> None:
    """ Save the current Words-dictionary to a file 
        with the given filename and path
    """
    try:
        with open(filename, "w") as file:
            jsoned = json.dumps(words)
            file.write(jsoned)
    except OSError as error:
        print("File error saving file:", error)
        # guard clause return
        return

    print("Succesfully saved dictionary to:", filename)

def load_json(filename: str) -> Dict[str, str]:
    with open(filename, "r", encoding="UTF-8") as file:
        read_file = file.read()
        print(read_file)
        # response = json.loads('{"sus":"amogus"}')
        # print(response)
    return {"sus": "amogus"}

print("Starting dictionary:", words)
print("Length of dictionary:", len(words))

# load_json("dictionary.json")
save_to_json("dictionary.json")
