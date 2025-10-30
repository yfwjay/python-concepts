# A simple function that returns the square of a number.
def square(num):
    return num * num

input = int(input("Enter a number to square: "))
result = square(input)
print(f"The square of {input} is: {result}")