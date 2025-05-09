
def authenticate_user():
    users = [
        {"name": "alaa", "pass": "123"},
        {"name": "ahmed", "pass": "456"}
    ]

    username = input("Enter username: ")
    user_found = False

    for user in users:
        if username == user["name"]:
            user_found = True
            password = input("Enter password: ")
            if password == user["pass"]:
                print("Authorized")
            else:
                print("Wrong password")
            break

    if not user_found:
        print("Wrong username")
