from fuel import convert, gauge
import pytest

def test_Zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_denGreaterthenNum():
    with pytest.raises(ValueError):
        convert("4/3")

def test_NotInt():
    with pytest.raises(ValueError):
        convert("4.0/5")

def test_Full():
    assert gauge(convert("4/4")) == "F"
    assert gauge(convert("99/100")) == "F"

def test_Empty():
    assert gauge(convert("0/4")) == "E"
    assert gauge(convert("1/100")) == "E"

def test_Normal():
    assert gauge(convert("3/4")) == "75%"