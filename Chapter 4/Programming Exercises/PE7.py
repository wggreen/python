days = int(input("How many days? "))
total = 0

for x in range(days):
    pay = 2**x
    total += pay
    print(x+1, "\t", pay)

total_pay = total * 0.01
print("The total earnings were", format(total_pay, '.2f'))
