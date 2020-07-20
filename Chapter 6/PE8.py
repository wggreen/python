def main():
    file = open('random.txt', 'r')
    lines = 0
    total = 0
    for line in file:
        lines += 1
        total += int(line)
    print("There are", lines, "lines in the file")
    print("The total of all the integers in the file is", total)
    file.close()

main()
        
