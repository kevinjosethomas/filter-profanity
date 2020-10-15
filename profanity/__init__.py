import os
import json
from .config import PROFANE_WORD_LIST_PATH


# Convert profane word list from json to array
with open(os.path.join(__file__, PROFANE_WORD_LIST_PATH), "r") as _profane_word_list:
    PROFANE_WORD_LIST = json.load(_profane_word_list)
