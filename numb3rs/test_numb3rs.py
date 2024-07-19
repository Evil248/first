from numb3rs import validate

def test_format():
    assert validate(r'2.4.6.8') == True
    assert validate(r'2.4.6') == False
    assert validate(r'2.4') == False
    assert validate(r'2') == False
def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'1000.255.255.255') == False
    assert validate(r'255.1000.255.255') == False
    assert validate(r'255.255.1000.255') == False
    assert validate(r'255.255.255.1000') == False
if __name__ == "__main__":
    test_format()
    test_range()


