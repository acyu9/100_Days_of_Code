import random
import Game_Data
from os import system

personA = random.choice(Game_Data.data)
personB = random.choice(Game_Data.data)
while personA == personB:
    personB = random.choice(Game_Data.data)


def choices(personA):
    """Randomly select personB and check if it's the same as personA. If so, choose again."""
    choice = random.choice(Game_Data.data)
    while choice == personA:
        choice = random.choice(Game_Data.data)
    return choice


def script():
    """Prints the two in competition."""
    print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}.")
    print("VS")
    print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess != 'A' and guess != 'B':
        exit("Follow the directions.")
    return guess


def play_game():
    score = 0
    loop = True
    # Global here so personA in while loop won't be unbound/local variable referenced before assignment
    global personA
    global personB

    # Check answer. Move higher counts to A and choose another random for B
    while loop:
        guess = script()
        if guess == "A" and (personA['follower_count'] > personB['follower_count']):
            personB = choices(personA)
            score += 1
            print(f"You're right! Current score: {score}.")
        elif guess == 'B' and (personB['follower_count'] > personA['follower_count']):
            personA = personB
            personB = choices(personA)
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry that's wrong. Final score: {score}.")
            loop = False

play_game()
while input("Play again? Type 'y' or 'n': ").lower() == 'y':
    system('cls')
    play_game()