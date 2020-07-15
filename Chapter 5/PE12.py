def main():
    def max(num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2

    number = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))

    maximum = max(number, number2)
    print(maximum, "is the bigger number")

main()
