
def validate_user_input():
    name = input("Enter your name: ")
    while name.strip() == "" or name.isdigit():
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")

    print("Name:", name)
    print("Email:", email)

    if "@" in email and "." in email:
        at_index = email.index("@")
        dot_index = email[at_index + 1:].find(".")
        if dot_index != -1:
            dot_index += at_index + 1
            if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
                print("Email is valid.")
                return
    print("Email is invalid.")
