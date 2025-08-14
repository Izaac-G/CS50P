import pytest
from working import convert

def test_valid_input():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("five thirty AM to nine PM")
    with pytest.raises(ValueError):
        convert("05:30 to 09:00")
    with pytest.raises(ValueError):
        convert("5:30 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("5:30 AM 9 PM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("5:60 AM to 9:60 PM")
    with pytest.raises(ValueError):
        convert("5:000 AM to 9:000 PM")
    with pytest.raises(ValueError):
        convert("5:5 AM to 9:5 PM")
    with pytest.raises(ValueError):
        convert("5:30.00 AM to 9:00.0 PM")
