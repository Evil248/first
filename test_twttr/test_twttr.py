from twttr import shorten
def main():
    test_up_low()
    test_numbers()
    test_ponc()

def test_up_low():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwIttER") == "TwttR"
def test_numbers():
    assert shorten('1234') == '1234'
def test_ponc():
    assert shorten('!?.,') == '!?.,'