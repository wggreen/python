def main():
    numbers = []
    for x in range(20):
        number = int(input("Enter a number: "))
        numbers.append(number)
    lowest = min(numbers)
    highest = max(numbers)
    total = 0
    for y in numbers:
        total += y
    average = total / 20
    print("The lowest number is", lowest)
    print("The highest number is", highest)
    print("The total is", total)
    print("The average is", format(average, '.2f'))
    
main()
