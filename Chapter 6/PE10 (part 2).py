def main():
    file = open('golf.txt', 'r')

    name = file.readline()
    while name != "":
        score = file.readline()
        
        name = name.rstrip('\n')
        score = score.rstrip('\n')

        print("Name:", name)
        print("Score:", score)
        print()

        name = file.readline()

    file.close()

main()
