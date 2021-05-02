def main():
    email = get_emails()
    email_dict = {}
    while email != "":
        name_list = email.split("@", 1)
        if "." in name_list[0]:
            name_list2 = name_list[0].split(".")
            name = " ".join(name_list2)
        elif name_list[0].isalpha() is False:
            name = " ".join([n for n in name_list[0] if n.isalpha()])
        else:
            name = name_list[0]
        choice = input("Is your name {}?(Y/n)".format(name.title())).upper()
        if choice == "N" or choice == "NO":
            names = input("Name: ")
            email_dict[names.title()] = email
        elif choice == "Y" or choice == "YES":
            email_dict[name.title()] = email
        email = get_emails()
    print(email_dict.items())


def get_emails():
    emails = input("Enter your emails: ")
    return emails


main()
