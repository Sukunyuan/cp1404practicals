def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    grade = score_grade(score)
    print(grade)


def score_grade(score):
    if 50 <= score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()

import random


def main2():
    score = random.randint(0, 100)
    grade = score_grades(score)
    print("Your score is {} that is {}".format(score, grade))


def score_grades(score):
    if 50 <= score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main2()
