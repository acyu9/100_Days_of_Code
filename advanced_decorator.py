# Create a logging_decorator()
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}")
        print("The arguments are " + str(args)) 
        #result = function(args[0], args[1], args[2])
        #print(result)
        # Alternatively, print with all args
        print(function(*args))
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a, b, c

a_function(1, 2, 3)