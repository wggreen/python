number = int(input("What's the starting number of organisms? "))
increase = int(input("What's the average daily increase? "))
days = int(input("How many days to multiply? "))

increase = 1 + (increase/100)

print("Day Approximate \tPopulation")

for x in range(1, days+1):
    if x > 1:
        number *= increase
    print(x, "\t", format(number, '.2f'))
