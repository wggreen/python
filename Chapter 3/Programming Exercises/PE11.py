number = int(input("How many books are you ordering? "))

if number < 2:
    print("You earned 0 points")
if number >= 2 and number < 4:
    print("You earned 5 points")
if number >= 4 and number < 6:
    print("You earned 15 points")
if number >= 6 and number < 8:
    print("You earned 30 points")
if number >= 8:
    print("You earned 60 points")
