from seasons import check

def main():
    test_check()
def test_check():
    assert check("2007-12-12") == ("2007", "12", "12")
    assert check("2007-2-2") == None
    assert check("December 3, 2007") == None

if __name__ == "__main__":
    main()
