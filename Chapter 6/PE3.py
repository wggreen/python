def main():
    name = input("What's the file's name? ")
    file = open(name, 'r')
    x = 1
    line = file.readline()
    while line != "":
        print(x, ": ", line, sep="")
        x += 1
        line = file.readline()

main()
        
