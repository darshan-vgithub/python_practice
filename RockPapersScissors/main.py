import random

def Rock_paper_scissors(attempts_left):
    if attempts_left == 0:
        print("Sorry, you've used all 3 attempts.")
        return

    choices = ["rock", "paper", "scissors"]
    user = input("Enter your choice (rock, paper, scissors): ").lower()

    if user not in choices:
        print("Invalid choice. Try again.")
        Rock_paper_scissors(attempts_left)  # retry same attempt
        return

    computer = random.choice(choices)
    print(f"You chose {user}, Computer chose {computer}.")

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("You Lose!")

    # Decrement attempts after valid play
    Rock_paper_scissors(attempts_left - 1)

# Start the game
Rock_paper_scissors(3)
