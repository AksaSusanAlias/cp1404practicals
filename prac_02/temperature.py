MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
"""


def main():
    print(MENU)

    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "C":

            celsius = float(input("Celsius: "))

            fahrenheit = covert_to_fahrenheit(celsius)

            print(f"Result: {fahrenheit:.2f} F")

        elif choice == "F":

            fahrenheit = float(input("fahrenheit_in: "))

            celsius = covert_to_celsius(fahrenheit)

            print(f"Result: {celsius:.2f} C")

        else:

            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def covert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)

    return celsius


def covert_to_fahrenheit(celsius):
    fahrenheit_in = celsius * 9.0 / 5 + 32

    return fahrenheit_in


main()
