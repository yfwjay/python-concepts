# Concatenation of strings. 
greetings = "Hello, How are you?"
response = "I am fine, thank you!"

# answer = greetings + " " + response
# print(answer)
print(greetings + " " + response)

# Repetition of strings
print(greetings * 2)

# Methods
print(greetings.upper())
print(response.lower())
print(greetings.replace("Hello", "Hi"))
print(greetings.split(","))
print(greetings.strip())
print(greetings.title())
print(len(greetings))

# Substring

print("How" in greetings)  # Output: True
print("Goodbye" in greetings)  # Output: False
print("Goodbye" not in greetings)  # Output: True