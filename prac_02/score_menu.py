

MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit
"""


def get_valid_score():
    while True:
        score = float(input("Enter a score between 0 and 100: "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score! Score must be between 0 and 100.")


def print_result(score):
    result = determine_result(score)
    print(f"Score: {score}, Result: {result}")


def show_stars(marks):
    asterisks = '*' * int(marks)
    print("\n" + asterisks)


def determine_result(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def main():
    score = get_valid_score()

    print(MENU)
    choice = input("Choose an option: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice, please select from the menu.")

        print(MENU)
        choice = input("Choose an option: ").upper()

    print("Thank You")


if __name__ == "__main__":
    main()
