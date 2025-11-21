

# def user_details():
#     # initialize an empty List
#     person = []
#     # take input from the user
#     while True:

#         name = input("Enter your name =").title().strip()
#         age = int(input("Enter your age = "))
#         skills = input("Enter skills proficient in = ").title().strip()

#         # Add user input to a dictionary

#         details = {
#             "Name" : name , 
#             "Age" : age ,
#             "Skills" : skills
#         }

#         # Append this to our list

#         person.append(details)

#         # Loop through our list

#         for indx , i in enumerate(person , start = 1):
#             print(f"{indx}.{i}")
#         break

# print(user_details())


# iterate for keys and items in the dictionary

performance = {
    "Name" : "James Kabuga" , 
    "Marks" : 80
}

print("=======KEYS IN THE DICTIONARY========")
for key in performance:
    print(key)


print("=====KEYS AND VALUES IN THE DICTINARY=======")
for key , value in performance.items():
    print(f"{key} -> {value}")


