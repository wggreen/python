import math

feet = int(input("How many square feet of wall space will be painted? "))
price = int(input("What's the price of the paint per gallon? "))

gallons = feet/112
if gallons > math.floor(gallons):
    gallons = int(math.ceil(gallons))

paint_cost = gallons * price
labor = (feet/112)*8
labor_cost = labor * 35
total_cost = price + labor_cost

print("\n", gallons, " gallons of paint will be needed", sep="")
print(format(labor, '.2f'),  " hours of labor will be required", sep="")
print("The paint will cost $", format(paint_cost, '.2f'), sep="")
print("Labor will cost $", format(labor_cost, '.2f'), sep="")
print("The job will cost $", format(total_cost, '.2f'), " in total", sep="")
