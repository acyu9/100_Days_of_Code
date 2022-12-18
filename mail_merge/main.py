# Use "r" for raw string to avoid \N character escape
with open(r"Input\Names\invited_names.txt") as file:
    # Saves lines as list and remove \n
    list = file.read().splitlines()

# Reads and saves the letter
with open(r"Input\Letters\starting_letter.txt") as file:
    letter = file.read()

# Create new letter for each name
for name in list:
    with open(fr"Output\ReadyToSend\letters_for_{name}.txt", "w") as file:
        file.write(letter.replace("[name]", name))
