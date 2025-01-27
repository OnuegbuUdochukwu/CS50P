from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_startingWithH():
    assert value("hi") == 20
    assert value("HI") == 20

def test_sentences():
    assert value("What's up") == 100
    assert value("How are you doing? ") == 20


