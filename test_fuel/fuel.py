def main():
    fraction = input("Fraction:")
    fraction_covered = convert(fraction)
    output = gauge(fraction_covered)
    print(output)
def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            new_x = int(x)
            new_y = int(y)
            f = new_x / new_y
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction:")
                pass
        except (ValueError,ZeroDivisionError):
            raise
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 90 :
        return "F"
    else:
        return str(percentage) + "%"
if __name__ == "__main__":
    main()



