import twttr
from twttr import shorten

def test_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_numbers():
    assert shorten("1234567890") == "1234567890"

def test_punctuation():
    assert shorten(",./") == ",./"

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
