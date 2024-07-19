from plates import is_valid
def main():
    test_alpha()
    test_start()
    test_middle()
    test_zero()
    test_punc()
def test_alpha():
    assert is_valid("AA") == True
    assert is_valid("ABCDFG") == True
    assert is_valid("A") == False
    assert is_valid("LKjHGFD") == False
def test_start():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
def test_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
def test_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
def test_punc():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 13') == False

if __name__ == "__main__":
    main()