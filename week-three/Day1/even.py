
# A function that checks if a number is even using boolean is_even

def is_even(number):
    return number % 2 == 0

number1 = int(input("Enter a number to check if its even or not : "))

result = is_even(number1)

print(f"{number1} is even: {result} ")

# Another way to check if a number is even using if-else statement

def even_number(number1):
    if number1 % 2 == 0:
        print(f"{number1} is an even number")
    else:
        print(f"{number1} is not an even number")

number1 = int(input("Enter a number to check if its even or not : "))
even_number(number1)

