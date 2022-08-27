print("Welcome to the tip calculator.")

# Ask and validate bill
bill = float(input("What was the total bill? $"))
if (bill <= 0):
    exit("Are you sure?")
decimal_places = str(bill)[::-1].find('.')
if (decimal_places >= 3):
    exit("Invalid bill.")

# Ask and validate tip    
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
if tip not in (10, 12, 15):
    exit("Follow the directions!")

# Ask and validate people splitting the bill
people = input("How many people to split the bill? ")
try :
    (int(people))
except ValueError:
    exit("You can't have part of a person!")
if (int(people) <= 0):
    exit("Please input actual human count.")

# Bill calculation
tip_percent = tip / 100 + 1
bill_per_person = bill * tip_percent / int(people)

# Round() function does not add a zero to format clean division to 2 decimal places
# {:} is format spec, .2f is precision of 2 with fixed-point number
rounded_bill = "{:.2f}".format(bill_per_person)

print("Each person should pay: $" + str(rounded_bill))