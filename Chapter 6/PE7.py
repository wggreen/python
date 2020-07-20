import random

def main():
    file = open('random.txt', 'w')
    number = int(input("How many numbers should be written to the file? "))
    for x in range(number):
        rand = str(random.randint(1,500))
        file.write(rand)
        file.write("\n")

main()
