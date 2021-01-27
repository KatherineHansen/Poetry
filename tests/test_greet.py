from greet import __version__


def test_version():
    assert __version__ == '0.1.0'

from greet.location import greet

def test_greet():
    result = greet("America/New_York")
    assert "New York!" in result
