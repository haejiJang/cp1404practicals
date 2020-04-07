'''
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
'''
total_cost = 0
number_of_items = int(input("How many items"))
while number_of_items < 0:
    print("Invalid number")
    number_of_items = int(input("How many items"))
for i in range(number_of_items):
    price = float(input("What is the price of item"))
    total_cost += price

if total_cost > 100:
    totalCost = price * 0.9

print("Total price for {} items is ${:.2f}".format(number_of_items, total_cost))

