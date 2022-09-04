import operator
from os import system

# Turns string operator to mathematical operator
ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}


# Calculator function
def calculate(first_number, operator, second_number):
    try:
        return ops[operator](first_number, second_number)
    except ZeroDivisionError:
        return


def calculator():
    to_continue = True
    # Validate user input
    try:
        first_number = float(input("Enter your first number: "))
    except ValueError:
        exit("Invalid input.")

    while to_continue:
        # Validate user input    
        operator = input("Choose an operator (+, -, *, /): ")
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            exit("Invalid operator.")
        try:
            second_number = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input.")
        
        # Call calculate function and store answer
        result = calculate(first_number, operator, second_number)
        if result == None:
            exit("Cannot divide by zero.")
        
        # Print answer
        print(f"{first_number} {operator} {second_number} = {result}")

        # Ask user what to do next
        keep_calculating = input(f"Type 'y' to continue calculating with {result} or " + 
            "type 'n' to start a new calculator or type 'exit' to stop the calculator: ")
        
        # Validate user input
        if keep_calculating != 'y' and keep_calculating != 'n' and keep_calculating != 'exit':
            exit("Follow the directions.")
        elif keep_calculating == 'y':
            first_number = result
        elif keep_calculating == 'n':
            # Clears terminal window
            system('cls')
            # False here to end the outer loop, or else outer loop goes again after inner loop is done
            to_continue = False
            # Recursive function
            calculator()
        else:
            to_continue = False


calculator()