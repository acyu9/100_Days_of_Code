alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    # Runs the program until user wants to stop ciphering
    run_again = "yes"
    while run_again: 
        caesar()
        run_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()


def caesar():
    # Validate user input for direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        exit("Follow the directions!")

    text = input("Type your message:\n").lower()
    # Validate user input for shift number
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        exit("Input a whole number.")

    secret_word = ""
    for char in text:
        # Preserve nonalphabetical char
        if not char.isalpha():
            secret_word += char
            continue
        # % 26 to ensure the alphabet circulates from z back to a
        if direction == "encode":
            shifted_index = (alphabet.index(char) + shift) % 26
        elif direction == "decode":
            shifted_index = (alphabet.index(char) - shift) % 26
        secret_word += alphabet[shifted_index]
    print(f"The {direction}d message is {secret_word}")



if __name__=="__main__":
    main()