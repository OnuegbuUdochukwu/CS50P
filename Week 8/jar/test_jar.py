from jar import Jar
import pytest

def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    with pytest.raises(ValueError):
        jar2 = Jar(capacity = -2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(capacity = 10)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(11)
    # jar.deposit(5)
    # jar.deposit(1)



def test_withdraw():
    jar = Jar(capacity = 10)
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(11)

test_str()