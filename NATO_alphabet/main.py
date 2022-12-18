import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Loop through rows of a dataframe and save key(letter):value(code) in a dictionary
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
loop_on = True
# Upper because the letters in the csv are uppercases
user_input = input("Eneter a word: ").upper()
while loop_on:
    try:
        output_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:    
        print(output_list)
        loop_on = False

# Alternative to Try Except        
# Check if there's nonalphabetical entry. If alphabet entered, then find the value of that key
#output_list = [nato_dict[letter] for letter in user_input if letter in nato_dict.keys()] 