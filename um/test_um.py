from um import count

def main():
    test_part_word()
    test_surrounded()

def test_part_word():
    assert count("yummy") == 0
    assert count("enterobacterium") == 0
    assert count("luminousness") == 0

def test_surrounded():
    assert count("um?") == 1
    assert count("um") == 1
    assert count("Um") == 1

if __name__ == "__main__":
    main()
