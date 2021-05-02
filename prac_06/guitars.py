from prac_06.guitar import Guitar


def main():
    """
    get information of guitars and print them
    """
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print_guitars(guitars)


def print_guitars(guitars):
    for i, guitar in enumerate(guitars):
        vintage_string = "(Vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


def get_guitars(guitars):
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")


main()