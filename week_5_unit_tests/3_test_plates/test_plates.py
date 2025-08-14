import plates
from plates import is_valid

def test_beginning():
    assert is_valid("12") == False

def test_lenth():
    assert is_valid("a") == False
    assert is_valid("asdfjkl") == False
    assert is_valid("asdfjk") == True

def test_for_zero():
    assert is_valid("aa0111") == False
    assert is_valid("aa1110") == True

def test_ending():
    assert is_valid("123456") == False
    assert is_valid("aa123a") == False
    assert is_valid("aa1234") == True

def test_punctuation():
    assert is_valid(".,.,") == False
    assert is_valid("aaa.") == False
