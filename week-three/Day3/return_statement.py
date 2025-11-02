# How return statements work in functions and differenciate from print statements

def greet(name):
    return f"Hello , {name}!"

result = greet("Alice")
print(result)  # This will print the returned value from the function


# Note: If we used print inside the function instead of return,
# the function would not return any value, and result would be None.

def greet_with_print(name):
    print(f"Hello , {name}!")   

result_print = greet_with_print("Bob")
print(result_print)  # This will print None since the function does not return anything


# Reason is the print statement once executed its not reusable, whereas return statement sends back a value that can be stored and used later.  