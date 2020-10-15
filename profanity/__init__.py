import os
import json
from .config import PROFANE_WORD_LIST_PATH


# Convert profane word list from json to array
with open(os.path.join(os.path.dirname(__file__), PROFANE_WORD_LIST_PATH), "r") as _profane_word_list:
    PROFANE_WORD_LIST = json.load(_profane_word_list)


def censor_profanity(text: str, censor: str = "*"):
    """Censors all profane words with the provided censor"""

    split_text = text.split()
    final_text = " ".join(split_text)

    if len(split_text) < len(PROFANE_WORD_LIST):
        for word in split_text:
            if word.lower() in PROFANE_WORD_LIST:
                final_text = final_text.replace(word, censor*len(word))
    else:
        for word in PROFANE_WORD_LIST:
            if word in split_text.lower():
                final_text = final_text.replace(word, censor*len(word))

    return final_text

def has_profanity(text: str):
    """Checks if the text contains any profane content and returns a boolean accordingly"""

    split_text = text.split()

    if len(split_text) < len(PROFANE_WORD_LIST):
        for word in split_text:
            if word.lower() in PROFANE_WORD_LIST:
                return True
    else:
        for word in PROFANE_WORD_LIST:
            if word in split_text.lower():
                return True

    return False
