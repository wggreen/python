miles_driven = float(input("How many miles have you driven? "))
gallons_used = float(input("How many gallons of gas have you used? "))
mpg = miles_driven / gallons_used
print("The car gets", format(mpg, '.1f'), "miles to the gallon")
