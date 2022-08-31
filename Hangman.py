import random
import Hangman_Words

chosen_word = random.choice(Hangman_Words.word_list)

print(f"{chosen_word}")

# Print _ for player
blanks = []
for i in chosen_word:
    blanks.append("_")

print(blanks)
lives = 6
counter = 0
letters_guessed = []

while "_" in blanks:
    guess = input("Guess a letter: ").lower()

    # Enumerate adds a counter, as oppose to index. Count gives the index.
    for count, char in enumerate(chosen_word):
        if guess == char:
            blanks[count] = guess
            counter += 1
    
    # If counter is 1+, that means the letter is correct; otherwise, deduct a life
    if counter < 1:
        lives -= 1
        letters_guessed += guess
    counter = 0
    
    if lives == 0:
        print("You lose!")
        break

    # Print for player info        
    print(f"You have {lives} lives left. Here are the letters you guessed already: {letters_guessed}")
    print(blanks)
    print("")

print("You win!")