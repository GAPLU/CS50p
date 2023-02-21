from numb3rs import validate

def test_valid():
    assert validate("0.255.0.255") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("136.253.42.1") == True


def test_invalid():
    assert validate("0.256.0.255") == False
    assert validate("-2.255.4.255") == False
    assert validate("0.255") == False
    assert validate("") == False
    assert validate("asd.255.0.2255") == False
    assert validate("hallo") == False