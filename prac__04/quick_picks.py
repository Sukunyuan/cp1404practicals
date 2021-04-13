import random


def main():
    picks = int(input("How many quick picks?"))
    for n in range(picks):
        quick = CONSTANTS()
        for i in quick:
            print(i, end=" ")
        print()


def CONSTANTS():
    constants = []
    for i in range(6):
        num = random.randint(1, 45)
        while num in constants:
            num = random.randint(1, 45)
        else:
            constants.append(num)
    return constants


main()
