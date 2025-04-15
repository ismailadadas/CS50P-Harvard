from twttr import shorten

def test_lowercase_vowels():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"

def test_uppercase_vowels():
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("HeLLo") == "HLL"
    assert shorten("TwItTeR") == "TwtTR"

def test_with_numbers():
    assert shorten("h3ll0") == "h3ll0"

def test_with_punctuation():
    assert shorten("Hi!") == "H!"

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_empty_string():
    assert shorten("") == ""

def test_full_sentence():
    assert shorten("This is a test.") == "Ths s  tst."
