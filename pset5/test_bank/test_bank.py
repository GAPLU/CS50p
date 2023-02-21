from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("What's up") == 100
    assert value("123") == 100
    assert value("") == 100