import pytest
from um import count

def test_valid():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um. . .") == 1
    assert count("Um") == 1

def test_words():
    assert count("Yum") == 0
    assert count("Yummy") == 0
    assert count("Umberella") == 0
    assert count("Album") == 0

def test_numbers():
    assert count("1um") == 0
    assert count("um1") == 0
    assert count("u1m") == 0
