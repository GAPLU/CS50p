from plates import is_valid

def test_first_two():
    assert is_valid("02CS50") == False
    assert is_valid("C0ASD") == False
    assert is_valid("0CS59") == False
    assert is_valid("CS50") == True

def test_size():
    assert is_valid("CS501020") == False
    assert is_valid("") == False
    assert is_valid("CS5012") == True

def test_order():
    assert is_valid("CS50A") == False
    assert is_valid("CSAS2F") == False
    assert is_valid("CS5060") == True
    assert is_valid("CSS04") == False

def test_case():
    assert is_valid("cs50") == True
    assert is_valid("CsS50") == True

def test_content():
    assert is_valid("CS,54") == False
    assert is_valid("CS 20") == False
    assert is_valid("ASDAS") == True
    assert is_valid("1231") == False