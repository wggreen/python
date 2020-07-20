def main():
    number = int(input("How many players are in the tournament? "))
    file = open('golf.txt', 'w')

    for x in range(1, number+1):
        print("Enter data for player", x)
        name = input("Name: ")
        score = input("Score: ")

        file.write(name + '\n')
        file.write(score + '\n')
        print()

    file.close()
    print("Player records written to golf.txt")

main()
