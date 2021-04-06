def main():
    password = get_password()
    if len(password) >= 6:
        for n in range(len(password)):
            print("*", end="")


def get_password():
    passwords = input("Enter your password: ")
    while len(passwords) < 6:
        print("Invalid password")
        passwords = input("Enter your password: ")
    return passwords


main()