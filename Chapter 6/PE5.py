def main():
    file = open('numbers.txt', 'r')
    total = 0
    line = file.readline()
    while line != "":
        number = int(line)
        total += number
        line = file.readline()
    print("The sum of the integers in the file is", total)

main()
