import random
options = ("rock", "paper", "scissors")
running = True
#For Playing multiple rounds, set running to True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("rock, paper, or scissors? ").lower()

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == 'paper':
            print("Computer wins!")
        else:
            print("Player wins!")
    elif player == "paper":
        if computer == 'scissors':
            print("Computer wins!")
        else:
            print("Player wins!")
    elif player == "scissors":
        if computer == 'rock':
            print("Computer wins!")
        else:
            print("Player wins!")

    print(f"Computer chose: {computer}")
    print(f"Player chose: {player}")
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        running = False

    
print("Thanks for playing!")