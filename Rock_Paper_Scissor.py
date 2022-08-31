# Make a list with 0 rock, 1 paper, 2 scissor
# Random choice by computer
# User input
# Compare computer and user

import random


rps = ["rock", "paper", "scissor"]
computer = random.randint(0, 2)

# Validate player input
try:
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
except ValueError:
    exit("Follow the directions!")
if player >= 3 or player < 0:
    exit("Invalid input. You lose.")

print(f"Computer chooses {rps[computer]}")

# Calculate result
if player == 0 and computer == 2:
    print("You win!")
elif computer == 2 and player == 0:
    print("Computer wins!")
elif computer > player:
    print("Computer wins!")
elif player > computer:
    print("You win!")
else:
    print("Draw.")


# Alternatively, could use a 3x3 matrix with the result (i.e. "You win!") defined then
# print rps[computer][player] 