import pytest
from seasons import date_checker, minutizer, sing

def test_dates():
    assert str(date_checker("1999-01-01")) == "1999-01-01"
    with pytest.raises(SystemExit):
        date_checker("January 1st, 1999")
    with pytest.raises(SystemExit):
        date_checker("January 1, 1999")
    with pytest.raises(SystemExit):
        date_checker("1999 01 01")
    with pytest.raises(SystemExit):
        date_checker("01-01-1999")

def test_minutizer():
    assert minutizer(1) == 1440

def test_sing():
    assert sing(100) == "One hundred"
    assert sing(1440) == "One thousand, four hundred forty"
