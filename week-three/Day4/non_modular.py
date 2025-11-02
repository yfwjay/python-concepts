# Ill try to greet James but in a non-modular way
print("Hello, What is your name?")

input_name = input("Enter your name: ")


def greet(name):
    print(f"Hello, {input_name}!")


greet("James")
