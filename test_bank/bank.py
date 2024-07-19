def main():
    text= input("Greeting:")
    value_to = value(text)
    print(f"${value_to}")
def value(text):
    text = text.lower().strip()
    if "hello" in text:
        return 0
    elif "h" == text[0]:
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()


