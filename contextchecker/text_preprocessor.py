
from imports import *

def remove_punctuation(text):
    """Function that takes in a string and removes all punctuation."""
    text = re.sub(r"[^\w\s]", "", text)
    return text

def tokenizer(text):
    words_no_punct = remove_punctuation(str(text).lower())
    return str(words_no_punct).split(' ')



