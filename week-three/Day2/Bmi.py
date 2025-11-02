# We first define a function called bmi_calculator taht takes in 2 parameters: weight and height

def bmi_calculator(weight , height):
    # We now use the formulae to calculate the BMI
    return weight / (height **2)

# We now ask the user to enter their weight in kg

user_weight = float(input("Enter your weight in kg: "))
# We now ask the user to enter their height in meters
user_height = float(input("Enter your height in meters: "))
# We now call the bmi_calculator function but tnow with the user inputs
answer = bmi_calculator(user_weight , user_height)
# We now format our output using a f-string print statement 

print(f"Your BMI is: {answer}")




# One may go ahead and add more features in this function such as an if_else statement to classify the BMI value into underweight, normal weight, overweight and obesity.

# You can add the if_ else statements below the print statement to classify the BMI value. or inside the function bmi_calculator itself.

# For example:
if answer < 18.5:
    print("You are underweight.")
elif 18.5 <= answer < 24.9:
    print("You have a normal weight.")
elif 25 <= answer < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
