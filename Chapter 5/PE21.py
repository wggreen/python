import random

def main():
    tie = True
    while tie:
        number = random.randint(1, 3)

        computer = ""
            
        if number == 1:
            computer = "rock"
        if number == 2:
            computer = "paper"
        if number == 3:
            computer = "scissors"

        play = input("rock, paper, or scissors? ")
        print("computer played", computer, "\n")

        if computer == play:
            print("It's a tie!\n")
            number = random.randint(1, 3)
        if computer == "rock" and play == "paper":
            print("You win! paper beats rock!\n")
            tie = False
        if computer == "paper" and play == "rock":
            print("You lose! paper beats rock!\n")
            tie = False
        if computer == "paper" and play == "scissors":
            print("You win! scissors beat paper!\n")
            tie = False
        if computer == "scissors" and play == "paper":
            print("You lose! scissors beats paper!\n")
            tie = False
        if computer == "scissors" and play == "rock":
            print("You win! rock beats scissors")
            tie = False
        if computer == "rock" and play == "scissors":
            print("You lose! rock beats scissors!\n")
            tie = False

main()
