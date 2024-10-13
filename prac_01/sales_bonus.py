"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
in a loop
"""
sales = float(input("Enter sales: $"))
while sales >= 0.0:
    if sales < 1000:
        bonus = 0.1 * sales
    else:
        bonus = (15/100) * sales
    print(f"Sales : ${sales}  Bonus : ${bonus}")
    sales = float(input("Enter sales: $"))
print("___END___")