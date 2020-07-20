def main():
    name = input("What's the name of the file? ")
    file = open(name, 'r')
    for x in range(5):
        line = file.readline()
        if line:
            print(line)

main()
