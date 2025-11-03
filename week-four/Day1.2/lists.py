mixed = ["James" , "Joy" , "Claire" , "Precious" , 4 , 2 , True]

print(type(mixed[-1])) # confirming if the last item in the list is of boolean type
print(mixed) # prints items in the list dispite them having different data_types

# indexing and it starts from 0
print(mixed[0])
print(mixed[-1])
print(mixed[3])

# slicing items in a list

print(mixed[0:4])
print(mixed[: 3])
print(mixed[-6 : -2])

# list methods

# append
mixed.append("Apple")
print(mixed)

# insert at a specific index

mixed.insert(1 , "3")
print(mixed)

# remove by value = removes james from the list mixed

mixed.remove("James")
print(mixed)

# pop method
mixed.pop() # to remove the last item in the list
# mixed.pop(3) removes the item at index 3 in the list
print(mixed)

# delete method

del mixed[0]

# sorting items in a list

numbers =  [1, 2 , 6 ,5, 8, 4]
numbers.sort()
print(numbers)

# reversing the items in a list. It will sort and then reverse
numbers.reverse()
print(numbers)