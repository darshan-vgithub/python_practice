import random
def rock_paper_scissor():
    print("Welcome to Rock Paper Scissor Game")

    choices=["rock","paper","scissor"]

    computer_choice=random.choice(choices)

    user_choice=input("Enter your choice in rock,paper,scissor: ").lower()
    print(f"Computer choice is {computer_choice} and your choice is {user_choice}")
    if user_choice not in choices:
        print("Invalid choice")
        return
    elif user_choice== computer_choice:
        print("Tie")
    elif user_choice=="rock" and computer_choice=="paper":
        print("You lose")
    elif user_choice=="rock" and computer_choice=="scissor":
        print("You win")
    elif user_choice=="paper" and computer_choice=="rock":
        print("You win")
    elif user_choice=="paper" and computer_choice=="scissor":
        print("You lose")
    elif user_choice=="scissor" and computer_choice=="rock":
        print("You lose")
    elif user_choice=="scissor" and computer_choice=="paper":
        print("You win")

rock_paper_scissor()