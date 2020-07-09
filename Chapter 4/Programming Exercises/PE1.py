days = 5

total = 0

for x in range(1, 6):
    number = int(input("How many bugs did you catch today? "))
    total += number

print("In 5 days, you caught ", total, " bugs", sep="")
