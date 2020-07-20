def main():
    try:
        file = open('numbers.txt', 'r')
        total = 0
        line = file.readline()
        lines = 0
        while line != "":
            try:
                number = int(line)
                total += number
                lines += 1
            except ValueError:
                print("There was an error in converting the string", line, "to an integer.")
            line = file.readline()
        average = total/lines
        print("The average of the integers in the file is", average)
        file.close()
    except IOError:
        print("There was an error in opening and reading data from the file.")

main()
