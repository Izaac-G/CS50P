from validators import email

def main():
    print(validate(input("What's your email address? ")))

def validate(user_email):
    return "Valid" if email(user_email) else "Invalid"

if __name__ == "__main__":
    main()
