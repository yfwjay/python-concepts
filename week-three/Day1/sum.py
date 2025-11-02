# A function that calculates the sum of three numbers
def add(num1 , num2 , num3):
    return num1 + num2 + num3
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

total = add(number1 , number2 , number3)
print(f"The total sum of {number1} , {number2} and {number3} is: {total}")
