"""
CP1404/CP5632 - Practical
Broken program to determine score status
get score
    if score is less than 0 or greater than 100 "display score"
    if score is greater than 49 or less than 90 display "Passable"
    if score is less than 50 display "bad"
or display "excellent"
"""

import random


def determine_result(score):
    if score < 0 or score > 100:

        return "Invalid Score! Enter score between 0 to 100"

    elif score < 50:

        return "Bad"

    elif score < 90:

        return "Passable"
    else:

        return "Excellent"


def main():
    score = float(input("Enter score: "))

    print(determine_result(score))

    score = random.uniform(0, 100)

    print(f"{score:.2f}")
    result = determine_result(score)
    print(result)


main()
