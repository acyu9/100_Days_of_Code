import Coffee_Materials
from decimal import Decimal

# Save nested dictionary in variable
espresso = Coffee_Materials.MENU["espresso"]
latte = Coffee_Materials.MENU["latte"]
cappuccino = Coffee_Materials.MENU["cappuccino"]
resources = Coffee_Materials.resources
money = 0


def str_to_dict(choice):
    """Change user input, in str, to match up to coffee dict"""
    if choice == "espresso":
        coffee = espresso
    elif choice == "latte":
        coffee = latte
    elif choice == "cappuccino":
        coffee = cappuccino
    return coffee


def update_ingredients(coffee):
    """Update resources list after coffee is ordered."""
    resources["water"] -= coffee["ingredients"]["water"]
    resources["coffee"] -= coffee["ingredients"]["coffee"]
    try:
        resources["milk"] -= coffee["ingredients"]["milk"]
    except KeyError:
        resources["milk"] = resources["milk"]
    return resources


def check_ingredients(coffee):
    """First check every ingredient."""
    message = ""
    if resources["water"] < coffee["ingredients"]["water"]:
        message += "Not enough water. "
    if resources["coffee"] < coffee["ingredients"]["coffee"]:
        message += "Not enough coffee. "
    try:
        if resources["milk"] < coffee["ingredients"]["milk"]:
            message += "Not enough milk."
    except KeyError:
        ...
    return message


def calculate_change(total, coffee):
    """Calculate change. If not enough money, return -1. If enough money, return change."""
    change = round(total - coffee["cost"], 2)
    # Round() alone didn't round to 2 decimal places. 
    income = round(Decimal(coffee["cost"]), 2)
    if change < 0:
        return False
    else:
        return change, income


def coffee_machine():
    global loop
    global resources
    global money
    income = 0
    
    # User input. Hidden inputs: report and off
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]} mL")
        print(f"Money: ${money}")
        return
    elif choice == "off":
        exit("Goodbye.")

    # Check if there's enough ingredients left
    message = check_ingredients(str_to_dict(choice))
    if message != "":
        exit(f"Sorry, there is: {message}")

    # User input for coins
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    # Total coins inserted into coffee machine
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    if choice != "espresso" and choice != "latte" and choice != "cappuccino":
        exit("That is not an option.")
    else:
        if not calculate_change(total, str_to_dict(choice)):
            exit("Sorry, that's not enough money. Money refunded.")
        else:
            # Increment income
            change, income = calculate_change(total, str_to_dict(choice))
            money += income
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice}. Enjoy!")
        resources = update_ingredients(str_to_dict(choice))


coffee_machine()
loop = True

while loop:
    coffee_machine()

