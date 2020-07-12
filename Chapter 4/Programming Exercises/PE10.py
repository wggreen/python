tuition = 8000
multiplier = 1
print("Year \tTuition")

for x in range(1, 6):
    multiplier += 0.03
    tuition *= multiplier
    print(x, " \t$", format(tuition, '.2f'), sep="")
    
