number = int(input("How many packages are being purchased? "))
total = number * 99

if number == 0:
    print("No packages were purchased")
if number > 0 and number < 10:
    print("There was no discount. The total is $", total, sep="")
if number >= 10 and number <= 19:
    total *= 0.9
    print("The discount was 10%. The total is $", format(total, '.2f'), sep="")
if number >= 20 and number <= 49:
    total *= 0.8
    print("The discount was 20%. The total is $", format(total, '.2f'), sep="")
if number >= 50 and number <= 99:
    total *= 0.7
    print("The discount was 30%. The total is $", format(total, '.2f'), sep="")
if number >= 100:
    total *= 0.6
    print("The discount was 40%. The total is $", format(total, '.2f'), sep="")
