# I'll be implimenting a list

# List definition

details = ["James" , "Joy" , 20 , 25 , 10 , True]

# List slicing

print(details[:2])  # Displays items from 1st index to index 2 but doesn't include items in index 2

print(details[::-1]) # Displays items from last to start. its will start with item from last position to 1st.

# List indexing
print(details[0]) #prints item at index 0
print(details[-1]) #prints the item in the last index.


# List methods

# Append method
# -> Adds items to the list

print("============APPEND============")
details.append("Hello")
print(details)

# insert at specific index
print("======AT SPECIFIC INDEX=======")
details[1] = "NVIDIA"
print(details)

# remove by value
print("===REMOVE BY VALUE=====")
details.remove("Hello")
print(details)

# pop method

print("======POP METHOD ===========")
details.pop(0)
print(details)

print("=====SORT ITEMS IN A LIST =====")

# Supports only items of int type
print("====ASCENDING ORDER======")
numbers = [1 ,4,6,3,2,8,10,90,4]
numbers.sort()
print(numbers)

print("=====DESCENDING ORDER======")
numbers.copy
numbers.sort(reverse=True)
print(numbers)


# ITERATING THROUGH A LIST
print("=========ITERARTING A LIST==========")

# create a new list

new_details = ["NVIDIA" , "SAMSUNG" , "IPHONE" , 20 , 40 , True , 10 , 13]

# we use a for loop

for indx , item in enumerate(new_details , start=1):
    print(f"{indx}.{item}")