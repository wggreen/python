def main():
    file = open('names.txt', 'r')
    line = file.readline()
    x = 0
    while line != "":
        x += 1
        line = file.readline()
    print("There are", x, "names in the file")

main()
        
