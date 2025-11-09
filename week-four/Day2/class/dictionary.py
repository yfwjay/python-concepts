# Create a dictionary person with several key value pairs

person = {
    "name" : "James" , 
    "age" : 23 ,
    "Occupation" : "Engineer"
}

print(person)

# How to access a specific value using brackets

print(person["name"])

# Accessing an element using .get method

print(person.get("name"))

# How to add elements in a dictionary

person["status"] = "Graduated"

print(person)

# How to update elements in a dictionary

person["age"] = 20

print(person["age"])

# How to remove items in a dictionary

# Using the pop method and delete

# person.pop("status")
# print(person["status"]) # receive an error as the key-value pair is already deleted.

# delete 

# del person["age"]
# print(person)

# If you run the command above you will notice the key and its respective value is missing.


# How to loop through respecive keys
print("======================Keys==============================")
for key in person:
    print(key)

# How to loop through respective values

print("=======================Values=================================")

for value in person.values():
    print(value)


# How to loop through both keys and values

print("=======================Keys and Values========================")

for key , value in person.items():
    print(f"{key} -> {value}")