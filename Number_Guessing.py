import random
from os import system


def compare(guess, answer):
    """Compare guess and actual number. Return 0 means correct guess."""
    if guess > answer:
        return "Too high. \nGuess again."
    elif guess < answer:
        return "Too low. \nGuess again."
    else:
        return 0


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level != 'easy' and level != 'hard':
        exit("Follow the directions.")
    elif level == 'easy':
        attempts = 10
        print("You have 10 attempts reamining to guess the number.")
    else:
        attempts = 5
        print("You have 5 attempts remaining to guess the number.")

    answer = random.randint(1, 100)
    correct = False

    while not correct:
        # Validate user input
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            exit("Read the directions.")
        result = compare(guess, answer)
        if result == 0:
            print(f"You got it! The answer is {guess}.")
            correct = True
        else:
            print(result)
            # Countdown on the attempt
            if attempts > 0:
                attempts -= 1
                print(f"You have {attempts} attemps remaining to guess the number.")
                # If out of attempts
                if attempts < 1:
                    print(f"You are out of guesses. The correct answer is {answer}.")
                    correct = True


play_game()

# Option to play the game again
while input("Do you want to play again? Type 'y' or 'n': ") == 'y':
    system('cls')
    play_game()
