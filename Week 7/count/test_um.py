from um import count

import pytest

def test_valid():
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2

def test_inWord():
    assert count("yummy") == 0
    assert count("yum") == 0

def test_surroundedBySpace():
    assert count(" um ") == 1
    assert count(" um um ") == 2
    assert count(" um um um ") == 3