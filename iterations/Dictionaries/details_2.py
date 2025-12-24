# I'll be defining a dictionary
# Use dictionary methods
# loop through the keys , values and all items in the dictionary.


# A dictionary is defined using curly braces.Takes 2 items: keys and values
details = {
    "Name" : "James" ,
    "Age" :  20 , 
    "Skills" : "Python , Sql , Data Visualisation"
}


# Access elements in the dictionary

print("=======ACCESS ALL ELEMENTS IN THE DICTIONARY")
print(details) # prints all elements in the dictionary


print("=========SPECIFIC ELEMENTS IN THE DICTIONARY========`\n")

# We'll loop through keys , values then all items in the dictionary.

print("========KEYS===========")

for key in details:
    print(key)

print("==========VALUES==========")

for value in details.values():
    print(value)

print("\n========FORMATTED KEYS=========")

for indx , key in enumerate(details , start = 1):
    print(f"{indx}.{key}")

print("\n========FORMATTED VALUES=========")

for indx , value in enumerate(details.values() , start = 1 ):
    print(f"{indx}.{value}")



# Adding  new element in our details dictionary

print("\n========ADD NEW ELEMENT IN OUR DICTIONARY========= ")
details["Country"] = "Kenya"

for indx , value in enumerate(details.values() , start = 1 ):
    print(f"{indx}.{value}")


# Can directly access a specific elememt in our dictioanary

# using .get method

print("\n==========GET METHOD=========")

print(details.get("Name"))

print("\n==========UPDATE ELEMENTS=========")

details["Name"] = "Kabuga" # change james to kabuga

for indx , value in enumerate(details.values() , start = 1 ):
    print(f"{indx}.{value}")



print("\n==========REMOVE ELEMENTS=========")

# Remove element at index 2

details.pop("Age")

for indx , value in enumerate(details.values() , start = 1 ):
    print(f"{indx}.{value}")









