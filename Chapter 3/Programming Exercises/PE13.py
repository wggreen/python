weight = float(input("How much does the package weight? "))

if weight > 0 and weight <= 2:
    cost = weight * 1.5
if weight > 2 and weight <= 6:
    cost = weight * 3
if weight > 6 and weight <= 10:
    cost = weight * 4
if weight > 10:
    cost = weight * 4.75
print("The package costs $", format(cost, '.2f'), sep="")

