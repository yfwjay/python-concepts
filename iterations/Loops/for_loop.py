numbers = [2,4,6,7,8,3,4,67,1,3,10,14,15,17 ]


# impliment a for loop to indicate if the numbers in our list are even or odd

print("============Iterating through lists============")
for index , i in enumerate(numbers , start=1):
    if i % 2 == 0:
        print(f"Position {index} = {i} -> Even")
    else:
        print(f"Position {index} = {i} -> Odd")

student = {
    "Name" : "James" ,
   " Age ": 20 , 
    "Skills ": "Data Engineer"
}

print("===========KEYS============")
for key in student:
    print(key)

print("===========VALUES=============")
for value in student.values():
    print(value)

print("============KEYS AND VALUES============")
for key , value in student.items():
    print(f"{key} -> {value}")


print("=====SKIP EVEN NUMBERS=========")
for i in numbers:
    if i % 2 == 0:
        continue
    else:
        print(f"{i} = Odd number")

print("=====SKIP ODD NUMBERS=========")
for i in numbers:
    if i % 2 != 0:
        continue
    else:
        print(f"{i} = Even number")



details = [2 ,5,6,7,"James" , "NVIDIA" , "SAMSUNG" , "IPHONE" , True]

# print("=======DISPLAY ONLY STRINGS IN THE LIST=======")
# # for i in details:
# #     if type(i) == type(int):
# #         continue
# #     else:
# #         print(i)

# for index , i in enumerate(details , start = 1):
#     if type(i) == "int":
#         continue
#     else:
#         print(i)
