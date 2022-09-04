from os import system

bidders = {}
loop = "yes"

# Create dictionary with name as key and bid as value
while loop == "yes":
    name = input("What is your name? ").title()
    # Validate user input
    bid = int(input("What is your bid? $"))
    if bid < 0:
        exit("Bid must be a positive integer.")
    bidders[name] = bid

    # Validate user input
    response = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if response != "no" and response != "yes":
        exit("Follow the directions!")
    elif response == "no":
        loop = "no"
    else:
        # Clears terminal window
        system('cls')

highest_price = 0
highest_bidder = ""
draws = {}

# Loop through the dictionary to see who has the highest bid
for bidder in bidders:
    bid = bidders[bidder]
    # Could just use the max function
    if bid > highest_price:
        highest_price = bid
        highest_bidder = bidder
    elif bid == highest_price:
        draws[bidder] = bid

# Cast because ".keys()" method returns a dict_keys object and
# to avoid Runtime Error when changing dict while iterating through it
draws_list = list(draws.keys())
for key in draws_list:
    if draws[key] < highest_price:
        del draws[key]

# If more than one person bids the same highest price, print all bidders
if len(draws) != 0:
    print("There is a draw between ", end="")
    for key in draws:
        print(key + " , ", end="")
    print(highest_bidder + f" with a bid of ${highest_price}!")
else:
    print(f"The winner is {highest_bidder} with a bid of ${highest_price}!")
