"""
get no_of_items
if no of items is less than 0 "display invalid number of items"
 For i in range starting from 0 up to no_of_item:
    Display "price of item" repeated no_of_item times.
total = total + price
if total is greater than 100 
discount = total * 10/100
total= total-discount
display"total" with 2 decimal places
 
"""
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))
total = 0
for i in range(0, number_of_items):
    price = float(input("Price of item : $"))
    total = total + price
if total > 100:
    discount = total * 0.1
    total = total - discount
print(f"Total price for {number_of_items} items is ${total:.2f}")