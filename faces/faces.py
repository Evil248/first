def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    user_input = input()
    result = convert(user_input)
    print(result)

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
