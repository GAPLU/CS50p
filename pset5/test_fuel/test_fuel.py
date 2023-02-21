from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    with pytest.raises(ValueError):
        convert("AS/100")
    with pytest.raises(ValueError):
        convert("120/100")
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"