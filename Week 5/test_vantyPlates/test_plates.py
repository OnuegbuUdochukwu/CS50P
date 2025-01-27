from plates import is_valid

def test_twoLettersStart():
    assert is_valid("HELLO") == True
    assert is_valid("HALO") == True
    assert is_valid("A222") == False


def test_greaterThanSix():
    assert is_valid("GOODBYE") == False
    assert is_valid("HELLO, WORLD") == False

def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AA22AA") == False
    assert is_valid("A2A2A2") == False
    assert is_valid("@#$%^&@") == False


def test_punctuation():
    assert is_valid("GOODBYE, ME") == False
    assert is_valid("HELLO, WORLD") == False
    
def test_alphaNumeric():
    assert is_valid("AA22AA") == False
    assert is_valid("A2A2A2") == False

