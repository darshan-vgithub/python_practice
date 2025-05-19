import random

def SnakeWaterGun(attempts_left):
    if attempts_left == 0:
        print("Sorry, you've used all 3 attempts.")
        return

    print("\nChoices: 0 = Snake, 1 = Water, 2 = Gun")
    try:
        n = int(input(f"Attempt {4 - attempts_left}/3 - Enter your number (0/1/2): "))
        if n not in [0, 1, 2]:
            print("Invalid input. Please enter 0, 1, or 2.")
            SnakeWaterGun(attempts_left)  # retry same attempt
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        SnakeWaterGun(attempts_left)  # retry same attempt
        return

    computer = random.randint(0, 2)
    choices = ['Snake', 'Water', 'Gun']
    print(f"You chose {choices[n]}, Computer chose {choices[computer]}.")

    if n == computer:
        print("It's a Tie!")
    elif (n == 0 and computer == 1) or (n == 1 and computer == 2) or (n == 2 and computer == 0):
        print("You Win!")
    else:
        print("You Lose!")

    SnakeWaterGun(attempts_left - 1)

# Start the game with 3 attempts
SnakeWaterGun(3)
