num1 = float(input("Enter the number 1 :"))
num2 = float(input("Enter the number 2 :"))

# The line below checks if the string type has been changed from string to a float.
# print(type(num_1))

print("Select an Operation")

print("1: Addition")
print("2: Subtraction")
print("3: Multiply")
print("4: Division")

operation = input("Enter Number corresponding to operation : ")

if operation == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}" )
elif operation == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}" )
elif operation == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}" )
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} * {num2} = {result}" )
    else:
        print("Error Division by 0")


