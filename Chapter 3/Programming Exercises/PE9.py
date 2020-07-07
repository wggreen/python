number = int(input("Please enter a number in the range of 0 to 36: "))
if number == 0:
    print("The pocket is green")
elif number % 2 == 0 and number > 0 and number <= 36:
    if (number >= 1 and number <= 10) or (number >= 19 and number <= 28):
        print("The pocket is black")
    else:
        print("The pocket is red")
elif number % 2 != 0 and number > 0 and number <= 36:
    if (number >= 1 and number <= 10) or (number >= 19 and number <= 28):
        print("The pocket is red")
    else:
        print("The pocket is black")
elif number < 0 or number > 36:
    print("Error. That number is outside the valid range")
