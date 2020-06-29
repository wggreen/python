price = float(input("How much did the meal cost? "))
tip = price * 0.18
tax = price * 0.07
total = price + tip + tax
print("The meal cost $", price)
print("The tip is $", format(tip, '.2f'))
print("Tax is $", format(tax, '.2f'))
print("The total is $", format(total, '.2f'))
