from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Igor") == "gr"
    assert shorten("Makima") == "Mkm"
    assert shorten("Name12") == "Nm12"
    assert shorten("I,you") == ",y"