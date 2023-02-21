from working import convert
import pytest

def test_plain():
    assert convert("3 AM to 5 PM") == "03:00 to 17:00"
    assert convert("6 PM to 4 AM") == "18:00 to 04:00"

def test_complex():
    assert convert("3:30 AM to 5:45 PM") == "03:30 to 17:45"
    assert convert("6:25 PM to 4:39 AM") == "18:25 to 04:39"

def test_invalid():
    with pytest.raises(ValueError):
        convert("13 AM to -2 PM")
    with pytest.raises(ValueError):
        convert("11:61 AM to 13:30 PM")
    with pytest.raises(ValueError):
        convert("My name is Igor")

