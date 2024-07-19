def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        for letter in s:
            if letter.isdigit():
                index=s.index(letter)
                if s[index:].isdigit() and int(letter) != 0:
                    return True
                else:
                    return False
        return True
main()