import random

num1 = random.randint(1, 1000)
num2 = random.randint(1, 1000)

total = num1 + num2

print(" ", num1, sep="")
print("+", num2, sep="")

answer = int(input("What's the total? "))

if answer == total:
    print("Congratulations! That's correct!")

else:
    print("That's incorrect")
