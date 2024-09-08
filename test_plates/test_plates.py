import plates

def test_alpha():
    assert plates.is_valid("522") == False

def test_letters():
    assert plates.is_valid("cs50") == True
    assert plates.is_valid("CS05") == False

def test_length():
    assert plates.is_valid("c") == False
    assert plates.is_valid("asdfghj") == False

def test_numbers():
    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AAA22A") == False

def test_period():
    assert plates.is_valid("ana,") == False
