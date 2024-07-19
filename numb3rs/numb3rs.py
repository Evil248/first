# В файле numb3rs.py
import re
import sys

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print(True)
        sys.exit(0)
    else:
        print(False)
        sys.exit(1)

def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        first_byte = int(ip.split(".")[0])
        if not 0 <= first_byte <= 255:
            return False
        list_of_n = ip.split(".")
        for number in list_of_n:
            if not 0 <= int(number) <= 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()

