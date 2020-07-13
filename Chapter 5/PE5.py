value = int(input("What's the actual value of a property? "))
assessment = value * 0.6
tax = assessment * 0.0072
print("The actual value of the house is $", value, sep="")
print("The assessed value of the house is $", format(assessment, '.0f'), sep="")
print("The property tax is $", format(tax, '.0f'), sep="")
