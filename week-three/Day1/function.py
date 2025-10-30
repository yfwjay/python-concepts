# Implimenting functions


# Function greet with a print statement
def greet():
    print("Hello! How are you?")
# We call the function to execute it
greet()


# Create a function that takes parameters
def greet_person(name):
    print(f"Hello {name}! Welcome aboard.")

# call the function greet_person with an argument
greet_person("James")


# functions that return values
def add_numbers(a, b):
    return a + b

# Call the function and store the result
result = add_numbers(5, 7)
print(f"The sum is: {result}")


# Function with default parameters
def greet_with_default(name="Guest"):
    print(f"Hello {name}! Welcome to our platform.")

# Call the function without an argument
greet_with_default()
# Call the function with an argument
greet_with_default("James")

# We try to impliment the user to enter their numbers and calculate the product
def multiply_numbers(x, y):
    return x * y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
product = multiply_numbers(num1, num2)
print(f"The product of {num1} and {num2} is: {product}")