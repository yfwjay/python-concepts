# # name = input("Enter your name: ")
# # print(type(name))

# # Various datatypes i remember string , integer , float, boolean , 
# name = "James"
# number = 1
# number_2 = 2.0
# is_even = True

# # print(type(name))
# # print(type(number))
# # print(type(number_2))
# # print(type(is_even))

# # Indexing and slicing

# print(name[1]) # first element in the name variable
# print(name[-1]) # Last element in the name variable
# print(name[:: -1]) #Reversing the string in the name variable


# # Slicing

# # print(name[:3])

# # string methods

# # Repetition

# # print(name * 3)

# # Concatenation

# # We combine various Strings together

# # name_1 = "Hello"
# # name_2 = "World"

# # print(name_1 + name_2)

# # Operations

# num_1 = 2
# num_2 = 3

# add = num_1 + num_2
# subtraction = num_1 - num_2
# product = num_1 * num_2
# quotient = num_1 / num_2
# power = num_1 ** 2
# modulus = num_1 % 2
# last_operation = num_1 // 4

# print(add)
# print(subtraction)
# print(product)
# print(quotient)
# print(power)
# print(modulus)
# print(last_operation)


# Calculator project

# Performs addition of two numbers

# We introduce the user to the calculator project
while True:
    intro = print("Hello , Welcome to the calculator \n")

    intro_2 = print("Hello , We will calculate the sum of 2 numbers \n")

    input_1 = int(input("Enter a number : "))
    input_2 = int(input("Enter the second number : "))

    answer = input_1 + input_2

    print(f"The sum of {input_1} and {input_2} is = {answer}")
