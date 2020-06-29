first_price = float(input("What's the price of the first item? "))
second_price = float(input("What's the price of the second item? "))
third_price = float(input("What's the price of the third item? "))
fourth_price = float(input("What's the price of the fourth item? "))
fifth_price = float(input("What's the price of the fifth item? "))
subtotal = first_price + second_price + third_price + fourth_price + fifth_price
tax = subtotal * 0.07
total = subtotal + tax
print("Subtotal:", format(subtotal, '.2f'))
print("Tax:", format(tax, '.2f'))
print("Total:", format(total, '.2f'))
