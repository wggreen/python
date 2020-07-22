import random

def main():
    numbers = []
    for x in range(7):
        numbers.append(random.randint(1,10))
    print("The lottery number is ", end="")
    for number in numbers:
        print(number, end="")

main()
