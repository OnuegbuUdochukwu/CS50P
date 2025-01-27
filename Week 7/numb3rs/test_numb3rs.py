from numb3rs import validate

def test_firstByte():
    assert validate("255.287.1255.3255") == False
    assert validate("3.343.665.1236") == False

def test_inValid():
    assert validate("256.6.276.0.5") == False
    assert validate("-3.3.-5.6.5") == False


# :( test_numb3rs.py catches numb3rs.py only checking if first byte of IPv4 address is in range
#     expected exit code 1, not 0
# :( test_numb3rs.py catches numb3rs.py accepting expecting five-byte IPv4 address
#     expected exit code 1, not 0