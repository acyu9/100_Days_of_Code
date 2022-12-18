# Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2


# Functions are first-class objects, can be passed around as arguments
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)   
# Outputs 5


# Functions can be nested in other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")
    
    nested_function()

outer_function()
# Calls outer_function > prints "I'm outer" >
# references to nested_function > calls nested_function > prints "I'm inner"


#Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")
    
    def one():
        print("one")
    
    def two():
        print("two")
    
    return nested_function, one, two

inner_function, a, b = outer_function()
# Calling outer_function > prints "I'm outer" > inner_function points to nested_function >
# a points to one > b points to two

inner_function(), b()
# Calling inner_function > executes nested_function > prints "I'm inner"
# Calling b > executes two > prints "two"


# Decorator example
from time import sleep

def delay_decorator(function):
    def wrapper_function():
        sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

# Same as 
decorated_function = delay_decorator(say_hello)
decorated_function()

say_hello()
# Both outputs 2 sec pause then printing "Hello" twice
# When calling the function, add the decorator to it

