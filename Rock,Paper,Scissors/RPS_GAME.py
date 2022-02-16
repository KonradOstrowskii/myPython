import random
from tracemalloc import stop

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock ,paper or scissors? : ").lower()
        if player == computer:
            print("computer : ", computer)
            print("player : ", player)
            print("Tie")
        elif player == "rock":
            if computer == "paper":
                print("computer : ", computer)
                print("player : ", player)
                print("Computer win")
            if computer == "scissors":
                print("computer : ", computer)
                print("player : ", player)
                print("Computer lose")
        elif player == "paper":
            if computer == "scissors":
                print("computer : ", computer)
                print("player : ", player)
                print("Computer win")
            if computer == "rock":
                print("computer : ", computer)
                print("player : ", player)
                print("Computer lose")
        elif player == "scissors":
            if computer == "paper":
                print("computer : ", computer)
                print("player : ", player)
                print("Computer win")
            if computer == "paper":
                print("computer : ", computer)
                print("player : ", player)
                print("Computer lose")

    playagain = input("Would You like to play again (yes/no) :")
    if playagain == 'no':
        break

print("Bye!!!! Have a nice day")
