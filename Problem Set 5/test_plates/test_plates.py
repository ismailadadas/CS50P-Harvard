from plates import is_valid

def test_valid_plate():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("PY123") == True

def test_length():
    assert is_valid("A") == False  # Too short
    assert is_valid("ABCDEFG") == False  # Too long

def test_start_with_letters():
    assert is_valid("CS50") == True   # valid
    assert is_valid("1CS50") == False  # starts with digit
    assert is_valid("C150") == False   # only first char is letter
    assert is_valid("123456") == False  # all digits


def test_number_rules():
    assert is_valid("CS05") == False  # starts with zero
    assert is_valid("CS50X") == False  # letters after number
    assert is_valid("CS5O") == False  # 'O' after a number is still a letter
    assert is_valid("CS500") == True  # valid format


def test_invalid_characters():
    assert is_valid("CS 50") == False  # space
    assert is_valid("CS.50") == False  # period
    assert is_valid("CS!50") == False  # punctuation
