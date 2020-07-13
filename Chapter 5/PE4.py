loan = int(input("What's your monthly loan payment? "))
gas = int(input("What's your montly gas expense? "))
oil = int(input("What's your monthly oil expense? "))
tires = int(input("What's your monthly tires expense? "))
maintenance = int(input("What's your monthly maintenance expense? "))

monthly = loan + gas + oil + tires + maintenance
annual_loan = loan * 12
annual_gas = gas * 12
annual_oil = oil * 12
annual_tires = tires * 12
annual_maintenance = maintenance * 12
annual_total = annual_loan + annual_gas + annual_oil + annual_tires + annual_maintenance

print("You'll spend $", annual_loan, " on loan payments per year", sep="")
print("You'll spend $", annual_gas, " on gas per year", sep="")
print("You'll spend $", annual_oil, " on oil per year", sep="")
print("You'll spend $", annual_tires, " on tires per year", sep="")
print("You'll spend $", annual_maintenance, " on maintenance per year", sep="")
print("You'll spend $", annual_total, " total per year", sep="")
