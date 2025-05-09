
def advanced_email_validation():
    def is_valid_email(address):
        if '@' in address and '.' in address:
            try:
                user, domain = address.split('@')
                subdomain, extension = domain.split('.')
                return bool(user and subdomain and extension)
            except ValueError:
                print("Invalid email format. Use exactly one '@' and one '.'")
        else:
            print("Email must contain '@' and '.'")
        return False

    attempts = 0
    email_input = input("Enter your email address: ")
    while not is_valid_email(email_input):
        attempts += 1
        if attempts == 3:
            print("You entered 3 incorrect email addresses!")
            break
        email_input = input("Enter a valid email address: ")
    else:
        print("Your email address is correct.")
