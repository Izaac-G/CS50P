import pytest
from fuel import convert, gauge

def test_conversion():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_value_error():
    with pytest.raises(ValueError):
        convert("asdf/fdsa")

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_percentage():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
