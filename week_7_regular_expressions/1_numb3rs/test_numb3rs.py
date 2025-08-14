import pytest
from numb3rs import validate

def test_valid_digits():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("249.199.99.9") == True

def test_invalid_digits():
    assert validate("999.999.999.999") == False
    assert validate("256.256.256.256") == False
    assert validate("255.255.255.2555") == False
    assert validate("255.900.900.900") == False

def test_invalid_format():
    assert validate("abc.def.ghi.jkl") == False
    assert validate("255") == False
    assert validate("255.255.255.255.255") == False
    assert validate("255.255.255.255.") == False
