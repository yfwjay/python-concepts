import random

# We creaate a variable and pass our random function to it with the range of numbers we want.
random = random.randint(1 , 10)

# We intialize a counter variable.
counter = 0

# We introduce the user to the game.
name = input("What is your name?  ")
print(f"Hello , {name} ! Welcome to the guessing game.")
print("I'm thinking of a number between 1 and 10.")

# We now create a while loop to allow the user to keep guessing until they get it right.
while True:
    # We ask the user to input their guess.
    guess = input("Take a guess between 1 and 10: ")
    # Now we have to make sure that what the user inputs is a number if not they get an error message and asked to try again.
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    # We now convert the guess to an integer through reassignment.
    guess = int(guess)
    # We increase the counter by 1 for each guess.
    counter += 1
    # We now check if the guess is correct, too low or too high.
    if guess < random:
        print("Your guess is too low. Try again.")
    elif guess > random:
        print("Your guess is too high. Try again.")
    else:
        print(f"Congratulations, {name}! You've guessed the number {random} correctly in {counter} attempts!")
        break
