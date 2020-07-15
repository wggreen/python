def main():
    present = int(input("What's the account's present value? "))
    interest = float(input("What's the monthly interest rate? ")) / 100
    months = int(input("How many months will the money be left in the account? "))

    def calculate_future_value(p, i, t):
        f = p * ((1 + i)**t)
        return f

    future = calculate_future_value(present, interest, months)
    print("The account's future value will be $", format(future, '.2f'), sep="")

main()
