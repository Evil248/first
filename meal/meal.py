def main():
    time = input("What is the time?")
    convert_time = convert(time)
    if 7 <= convert_time <= 8:
        print("breakfast time")
    elif 12 <= convert_time <= 13:
        print("lunch time")
    elif 18 <= convert_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes)/60)
    return hours

if __name__ == "__main__":
    main()