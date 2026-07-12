import random
import string

def random_text():
    letters = string.ascii_letters
    result = ""
    while not result.endswith("n"):
        result += random.choice(letters)
    return result
