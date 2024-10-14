"""
CP1404/CP5632 - Practical3
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# And with f-string formatting, introduced in Python 3.6
print(f"{year} {name} for about ${cost:,.02f}!")

for i in range(11):
    print(f"2 ^ {i:<2} is {2**i:>4}")


