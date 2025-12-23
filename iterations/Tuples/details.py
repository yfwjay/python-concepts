# A tuple is defined using parenthesis

# A Tuple is a collection of ordered , immutable list of items

# see example below:

person = ("James" , 20 , "Nyeri" , "Python" ,"True")

# we print the type of person to see if we have defined a tuple or not

print(type(person)) # should see class tuple

# Print the contents of our tuple

print(person) # outputs the content of our tuple person

print("========ATTEMPT TO CHANGE CONTENT OF TUPLE==========")

print("\n========UNCCOMMENT AND RUN THE COMMANDS HERE ==========")
# person[0] = "Kabuga"

# print(person) 

# if you try running the above command should expect a "type error" as tuples don't support changing elements within themselves.

print("\n====TUPLE ACCESS========")

# Access elements at index 0

print(person[0])  

print("\n======TUPLE SLICING========")

print(person[0:3])

print("===========TUPLE UNPACKING=========")

(num_1 ,num_2, num_3 , num_4 , num_5) = person

print(num_1) # ouputs james as we assigned james to num_1

print("======UNPACK FIRST AND LAST ITEM=========")

num_1 , *mid, num_last = person

print(num_1) # ouputs 1st element in our tuple
print(*mid) # ouputs the middle elements in our tuple
print(num_last) # ouputs the last element in our tuple

