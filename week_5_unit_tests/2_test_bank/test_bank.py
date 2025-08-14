import bank
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("howdy") == 20
    assert value("HOWDY") == 20

def test_else():
    assert value("cowboy") == 100
    assert value("1234") == 100
    assert value (".,/") == 100
