years = int(input("How many years are being measured? "))

total = 0

for year in range(1, years+1):
        for month in range(1, 13):
            print("\nYear ", year, ", month ", month, sep="")
            rain = int(input("How much rain this month? "))
            total += rain

months = years * 12
average = total / months
print("\nAfter ", months, " months, the total rainfall was ", total, " inches. The average rainfall per month was ", format(average, '.2f'), " inches.", sep="")
            
