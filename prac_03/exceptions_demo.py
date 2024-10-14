"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? In this scenario,
Ans) a `ValueError` will be triggered if the user provides
    an input that cannot be interpreted as an integer.
    For instance, if they enter a string such as `"abc"`
    or a decimal value like `"3.14"` when prompted for either
    the numerator or the denominator, the error will occur.
2. When will a ZeroDivisionError occur?
Ans) A ZeroDivisionError occurs when the denominator is set to
    0, dividing by zero is undefined in mathematics.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the non zero integer: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
