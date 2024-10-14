"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit

While choice is not "Q":
    If choice is "C":
        Prompt the user for a Celsius temperature and store it in celsius
        Calculate fahrenheit as (celsius * 9.0 / 5) + 32
        Display "Result: " concatenated with fahrenheit formatted to 2 decimal places 
    Else if choice is "F":
        Prompt the user for a Fahrenheit temperature and store it in fahrenheit
        Calculate celsius as 5 / 9 * (fahrenheit - 32)
        Display "Result: " concatenated with celsius formatted to 2 decimal places 
    Else:
        Display "Invalid option"
    
    Display MENU
    converted to uppercase

Display "Thank you."

"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

