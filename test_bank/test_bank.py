from bank import value
def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()


def test_return_zero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('Hello GI') == 0
def test_return_twenty():
    assert value('hey') == 20
    assert value('Hey gi') == 20
    assert value('Hi') == 20
def test_return_hundred():
    assert value("good morning") == 100
    assert value("Good Morning") == 100