from um import count

def test_corners():
    assert count("um asdadsum sadfasdfasdf um") == 2
    assert count("Um asdfsadf asdfum um asdf um") == 3
    assert count("uM um am fum atum") == 2

def test_plain():
    assert count("I, um, have not done it, um") == 2
    assert count("Um...") == 1

def test_invalid():
    assert count("I ate something yummy") == 0
    assert count("") == 0
    assert count("1232,a..zsa ") == 0



