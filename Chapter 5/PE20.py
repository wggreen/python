import random

def main():
    number = random.randint(1, 100)
    guess = 0
    guesses = 0
    
    while guess != number:
        guess = int(input("Guess the random number: "))
        guesses += 1
        if guess < number:
            print("Too low, try again.")
        if guess == number:
            print("Congratulations! That's correct.")
            print("That took you", guesses, "guesses.")
            print("Generating a new number...\n")
            number = random.randint(1, 100)
            guess = 0
            guesses = 0
        if guess > number:
            print("Too high, try again.")
            
main()
