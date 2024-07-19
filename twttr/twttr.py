def main():
    text = input("Input: ")
    result_vowles = shorten(text)
    print("Output:" + result_vowles)

def shorten(text):
    result_vowles = ""
    for letter in text:
        if not letter.lower()  in ['a', 'u', 'o', 'i', 'e']:
                result_vowles += letter
    return result_vowles

if __name__ == "__main__":
    main()