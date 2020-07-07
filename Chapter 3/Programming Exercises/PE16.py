year = int(input("What year is it? "))

if year % 100 == 0 and year % 400 == 0:
    print("It's a leap year. February has 29 days this year.")
else:
    print("It's not a leap year. February has 28 days this year.")
