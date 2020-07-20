def main():
    file = open('numbers.txt', 'r')
    total = 0
    line = file.readline()
    lines = 0
    while line != "":
        lines += 1
        number = int(line)
        total += number
        line = file.readline()
    average = total/lines
    print("The average of the integers in the file is", average)
    file.close()

main()
