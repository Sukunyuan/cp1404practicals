"""displays all of the odd numbers between
1 and 20 with a space between each one."""


def main1():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()


main1()

"""a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100"""


def a():
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()


a()

"""b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1"""


def b():
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()


b()

"""print n stars. Ask the user for a number, then print that many stars (*), all on one line"""


def c():
    number = int(input("Number of star: "))
    for i in range(number):
        print("*", end=' ')
    print()


c()

"""d. print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting at 1. 
"""


def d():
    number = int(input("Number of star: "))
    i = 0
    while i in range(number):
        n = 0
        while n <= i:
            print("*", end=' ')
            n += 1
        print()
        i += 1


d()
