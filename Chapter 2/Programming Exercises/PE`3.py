p = float(input("What's the principal? "))
r = float(input("What's the annual interest rate paid by the account? "))/100
n = int(input("How many times a year is the interest compounded? "))
t = int(input("How many years will the acount be left to earn interest? "))

a = p * (1 + (r/n))**(n*t)

print("After", t, "years, there'll be $", format(a, '.2f'), "in the account")
