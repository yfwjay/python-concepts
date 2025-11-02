# A function that concatenates two strings
def conactenate_strings(str1, str2):
    return str1 + " " + str2

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
result = conactenate_strings(string1, string2)
print(f"The concatenated string is: {result}")

# Method 2 of cancatenating two strings using print statement
def add_strings(str1, str2):
    print(f"The concatenated string is {str1 + str2}")

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
add_strings(string1, string2)

# Repeating a string 3 times
def repeat_string(str1):
    return str1 * 3
string1 = input("Enter a string to repeat: ")
result = repeat_string(string1)
print(f"The string repeated 3 times is: {result}")