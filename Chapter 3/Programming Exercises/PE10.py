print("Your goal is to ente the number of coins required to make exactly one dollar.")

pennies = int(input("\nHow many pennies? "))
nickels = int(input("How many nickels? "))
dimes = int(input("How many dimes? "))
quarters = int(input("How many quarters? "))

sum = (pennies * 1) + (nickels * 5) + (dimes * 10) + (quarters * 25)

if sum == 100:
    print("Congratulations! That's a dollar!")
elif sum > 100:
    print("That's more than a dollar")
elif sum < 100:
    print("That's less than a dollar")
