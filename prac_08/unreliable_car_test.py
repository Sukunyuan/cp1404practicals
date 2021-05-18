from prac_08.unreliable_car import Unreliable


def main():
    Car1 = Unreliable("Prius 1", 100, 80)
    Car2 = Unreliable("BMW 530", 100, 6)
    Car1.drive(5)
    Car2.drive(5)
    print(Car1)
    print(Car2)


main()