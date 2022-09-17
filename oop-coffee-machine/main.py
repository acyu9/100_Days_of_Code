from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects of classes
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def coffee_machine():
    global loop
    # Ask for user's entry
    choice = input("What would you like? (" + menu.get_items() + "): ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        return
    elif choice == "off":
        exit("Goodbye.")
    elif choice == "espresso" or choice == "latte" or choice == "cappucino":
        # Find_drink returns an object of the MenuItem
        # The order object contains the name, ingredients, and cost of the coffee already,
        # so no need to make our own objects of MenuItem
        order = menu.find_drink(choice)

        # If not enough resource, return False and sorry message
        # If not enough money, return False and sorry message
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
        else:
            loop = False
    else:
        exit("Invalid input.")


loop = True
while loop:
    coffee_machine()