from validator_collection import email

def main():
    email_adress = input("What's your email address? ")
    try:
        check = email(email_adress)
        print("Valid")
    except ValueError:
        print("Invalid")

if __name__ == "__main__":
    main()