# Names of self and person
# Number of TRUE letters = ten's place
# Number of LOVE letters = one's place

def main():
    # Ask for names and change to lowercase
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n").lower()
    name2 = input("What is their name? \n").lower()

    # Count true and love letters in both names
    true = count_true(name1) + count_true(name2)
    love = count_love(name1) + count_love(name2)

    # Combine the digits, not add, then change to int
    score = str(true) + str(love)
    int_score = int(score)

    # Check score and output message
    if (int_score < 10) or (int_score > 90):
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif (int_score >= 40) and (int_score <= 50):
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}")


def count_true(name):
    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")
    true= t + r + u + e
    return true


def count_love(name):
    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    e = name.count("e")
    love = l + o + v + e
    return love


if __name__=="__main__":
    main()


# A shorter way is to use sum(name.count(x)) for x in ("t", "r", "u", "e")