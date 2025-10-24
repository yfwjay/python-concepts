# A while loop to print even number between 1 and 20

number = 1

while number <= 20:
    if number % 2 == 0:
        print(f"{number} , is an even number.")
        number += 1
    