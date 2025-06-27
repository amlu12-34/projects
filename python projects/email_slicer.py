def email_slicer():
    email = input("Enter your email address: ").strip()

    if "@" in email and "." in email:
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email address. Please try again.")
email_slicer()
