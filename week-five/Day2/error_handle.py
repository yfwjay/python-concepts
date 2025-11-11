# Will generate a system that accepts 2 integers and performs its quotient. In return we will include the try-except handling



try:
    a = int(input("Enter a number = "))
    b = int(input("Enter the second number = "))
    result = a / b
    print(f"Dividing {a} / {b}")
    print(f"The quotient = {result}")
except ZeroDivisionError:
    print("You can't divide a number by 0 !!")
except ValueError:
    print("Enter a Valid number !!")

