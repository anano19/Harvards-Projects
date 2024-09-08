import pytest
import fuel

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/4") == 25
    assert fuel.convert("2/4") == 50
    assert fuel.convert("3/4") == 75

    with pytest.raises(ValueError):
        fuel.convert("cat")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
    with pytest.raises(ValueError):
        fuel.convert("3/2")

def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(75) == "75%"

