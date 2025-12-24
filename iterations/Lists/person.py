# Defining a List

person = ["James" , 20 , "Student" , "Nyeri"]
print(person)


# List indexing

print("============List Indexing==========")
item_1 = person[0]
print(item_1) # prints James as is the 1st item in the list

# List Slicing
print("===============List Slicing=================")
slice_1 = person[0:3]
slice_2 = person[::]
print(slice_1)
print(slice_2)

# Several Lists methods

# I'll impliment the following list methods
# pop , delete , remove , append, copy , insert , rreverse

print("======List Methods==========")

print("=====Append==========")
person.append("Math")
person.append("English")
print(person) #Adds math and English at the last index in the list person

print("========Remove===========")
person.remove("Math")
print(person) # Removes the Last item in the index

print("=================Pop=================")
person.pop(-1)
print(person) # Removes item at index -1. the last item

# Difference between pop and remove is pop = index and remove = value.

print("=========Insert==============")

person[-1] = "French" 
print(person)

print("============Sort Desccending=============")

numbers = [1 ,4,5,7,1,4,90,7,5,4,8,9,7,5,3,1,13,5]
numbers.sort() 
print(numbers)

print("============Sort Ascending=============")

numbers.sort(reverse = "True")
print(numbers)


print("============Iterating Through a List=============")

for i in person:
    print(i)

print("===========Formatted Iteration=========")
for indx , item in enumerate(person , start = 1):
    print(f"{indx} -> {item}")



