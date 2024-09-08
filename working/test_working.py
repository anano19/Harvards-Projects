import pytest
from working import convert


def test_convert_one():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'



def test_convert_two():
    with pytest.raises(ValueError):
        convert("0:30 am")

def test_convert_three():
    with pytest.raises(ValueError):
        convert("25:00 pm")

def test_convert_four():
    with pytest.raises(ValueError):
        convert("25:00 am")

def test_convert_five():
    with pytest.raises(ValueError):
        convert("12:65")

def test_convert_six():
    with pytest.raises(ValueError):
        convert("7:00 XM")

def test_convert_seven():
    with pytest.raises(ValueError):
        convert("8 am  to  5 pm")








