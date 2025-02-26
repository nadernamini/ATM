"""
Utility file containing methods used sporadically across modules.
"""

import random
import string


def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
