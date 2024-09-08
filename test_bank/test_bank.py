import bank


def test_hello():
    assert bank.value("hello") == 0

def test_h():
    assert bank.value("hi") == 20
    assert bank.value("HI") == 20

def test_else():
    assert bank.value("world") == 100
