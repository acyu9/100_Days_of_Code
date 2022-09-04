import random
from os import system

# Deck of cards with Ace = 11 and JQK = 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Ask and validate user input
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play != 'y' and play != 'n':
    exit("Follow the directions.")
elif play == 'n':
    exit("Ok, bye.")


def starting_deck():
    """Returns a k sized list of elements"""
    return random.choices(cards, k=2)


def calculate(deck):
    # Check for blackjack
    if sum(deck) == 21 and len(deck) == 2:
        return 0

    # Ace is 11 below 21 and 1 above 21
    for i in range(len(deck)):
        if sum(deck) > 21 and deck[i] == 11:
            deck[i] = 1
            print(deck)
    deck_sum = sum(deck)
    return deck_sum


def compare_score(player_score, computer_score):
    """Goes through the rules and returns who wins"""
    if computer_score == player_score:
        return "Draw."
    elif computer_score == 0:
        return "Computer has Blackjack. You lose."
    elif player_score == 0:
        return "You win with Blackjack!"
    elif player_score > 21:
        return "You went over 21. You lose."
    elif player_score < computer_score or computer_score > 21:
        return "You lose."
    else:
        return "You win!"


def play_game():
    player_deck = starting_deck()
    computer_deck = starting_deck()
    loop = True

    while loop:
        player_sum = calculate(player_deck)
        computer_sum = calculate(computer_deck)

        # Game ends if there's Blackjack or bust (over 21)
        if player_sum == 0 or computer_sum == 0 or player_sum > 21:
            break

        print(f"Your cards: {player_deck}, current score: {player_sum}")
        print(f"Computer's first card: {computer_deck[0]}")

        # Ask and validate user input
        to_continue = input("Type 'y' to add another card, type 'n' to pass: ").lower()
        if to_continue != 'y' and to_continue != 'n':
            exit("Invalid input.")
        elif to_continue == 'y':
            player_deck.append(random.choice(cards))
            # Computer draws as long as sum is < 17 or not at blackjack
            if computer_sum != 0 and computer_sum < 17:
                computer_deck.append(random.choice(cards))
        else:
            loop = False

    # Print result
    print(f"Your final hand: {player_deck}, final score: {player_sum}")
    print(f"Computer's final hand: {computer_deck}, final score: {computer_sum}")
    print(compare_score(player_sum, computer_sum))

    # Recursive function to play game again
    play_again = input("Do you want to play Blackjack again? Type 'y' or 'n': ")
    if play_again != 'y' and play_again != 'n':
        exit("Invalid input.")
    elif play_again == 'n':
        exit("Goodbye.")
    else:
        system('cls')
        play_game()


play_game()