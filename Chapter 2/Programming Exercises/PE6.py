price = 10.55
state_tax = price * 0.05
county_tax = price * 0.025
total = price + state_tax + county_tax
print("The price of the item is $", price, sep="")
print("The state tax is $", format(state_tax, '.2f'), sep="")
print("The county tax is $", format(county_tax, '.2f'), sep="")
print("The total is $", format(total, '.2f'), sep="")
