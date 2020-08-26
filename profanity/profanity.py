import os
import json
import time
import random
from .data.list import *
from fuzzywuzzy import fuzz

class Profanity:

    def __init__(self):
        """Initializes the Profanity Class"""
        pass


    @staticmethod
    def censor(text: str, censor_character: str = "*") -> str:
        """Censors obscene language in the text provided with censor_character"""

        time1 = time.time()
        split_text = text.split()
        censor_character = list(censor_character)
        print(f"Split and List = {time.time() - time1}")

        def random_char(length):
            time1 = time.time()
            string = ""
            for i in range(length):
                string += random.choice(censor_character)
            print(f"Random Char = {time.time() - time1}")
            return string

        found_words = []
        if len(split_text) > len(BANNED_WORD_LIST):
            for word in BANNED_WORD_LIST:
                time1 = time.time()
                for text_word in [split for split in split_text if fuzz.token_set_ratio(word, split) > 90]:
                    found_words.append(text_word)
                print(f"For Loop with Fuzzy1 = {time.time() - time1}")
        else:
            for word in split_text:
                time1 = time.time()
                for banned_word in [BANNED_WORD for BANNED_WORD in BANNED_WORD_LIST if fuzz.token_set_ratio(BANNED_WORD, word) > 90]:
                    found_words.append(word)
                print(f"For Loop with Fuzzy2 = {time.time() - time1}")

        time1 = time.time()
        censored_text = text
        for word in found_words:
            censored_text = censored_text.replace(word, random_char(len(word)))
        print(f"Replacement = {time.time() - time1}")

        return censored_text
