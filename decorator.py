import time

current_time = time.time()
#print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        initial_time = time.time()
        function()
        final_time = time.time()
        run_speed = final_time - initial_time
        print(f"{function.__name__} run speed: {run_speed}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator    
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()