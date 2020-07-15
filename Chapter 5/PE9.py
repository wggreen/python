sales = int(input("What's the total sales for the month? "))

county = sales * 0.025
state = sales * 0.05
total = county + state

print("The county sales tax will be $", format(county, '.2f'), sep="")
print("The state sales tax will be $", format(state, '.2f'), sep="")
print("The total sales tax will be $", format(total, '.2f'), sep="")
