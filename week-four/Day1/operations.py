def addition():
        num_1 = int(input("Enter a number= "))
        num_2 = int(input("Enter the second number= "))
        answer = num_1 + num_2
        print(f"The sum of {num_1} and {num_2} is = {answer}")
     
def subtraction():
     num_1 = int(input("Enter a number= "))
     num_2 = int(input("Enter the second number= "))
     answer = num_1 - num_2
     print(f"The difference of {num_1} and {num_2} is = {answer}")
def division():
     num_1 = int(input("Enter a number= "))
     num_2 = int(input("Enter the second number= "))
     answer = num_1  / num_2
     print(f"The quotient of {num_1} and {num_2} is = {answer}")
def multiplication():
     num_1 = int(input("Enter a number= "))
     num_2 = int(input("Enter the second number= "))
     answer = num_1 * num_2
     print(f"The product of {num_1} and {num_2} is = {answer}")
def is_even():
     while True:
          num_1 = int(input(("Enter a number to check if its even or not = ")))
          if num_1 % 2 == 0:
               print(f"{num_1} is an even number")
               break
          else:
               print(f"{num_1} is an odd number")
               break
def is_odd():
     while True:
          num_1 = int(input("Enter a number to check if its odd or not = "))
          if num_1 % 2 != 2:
               print(f"{num_1} is an odd number")
               break
          else:
               print(f"{num_1} is an even number")
               break
def exit_application():
        print("Goodbye! You have successfully exited the application .")
