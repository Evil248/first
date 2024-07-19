from validators import email

def main():
    user_email = input("What's your email address? ")
    if is_valid_email(user_email):
        print("Valid")
    else:
        print("Invalid")

def is_valid_email(email_address):
    return email(email_address)

if __name__ == "__main__":
    main()
