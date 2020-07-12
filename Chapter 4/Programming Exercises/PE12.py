number = int(input("Enter a number: "))
sum = 1

for x in range(1, number+1):
    sum *= x
print("The factorial of", x, "is", sum)
