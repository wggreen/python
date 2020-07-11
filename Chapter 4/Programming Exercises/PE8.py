number = int(input("Enter a number: "))
total = 0

while number > 0:
    total += number
    number = int(input("Enter a number: "))

print("The sum of positive numbers entered is", total)
