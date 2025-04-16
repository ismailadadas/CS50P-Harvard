from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello, world") == 0
    assert value("Hello, world") == 0


def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HI") == 20
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("HEY") == 20
    assert value("h") == 20
    assert value("H") == 20


def test_other_greetings():
    assert value("what's up") == 100
    assert value("good morning") == 100
    assert value("") == 100
    assert value("123") == 100
    assert value("!@#$") == 100
