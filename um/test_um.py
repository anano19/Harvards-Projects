from um import count

def test_um_one():
    assert count("hello, um") == 1


def test_um_two():
    assert count("hello, um, world, um") == 2


def test_um_three():
    assert count("yummy") == 0


def test_um_four():
    assert count("UM") == 1
