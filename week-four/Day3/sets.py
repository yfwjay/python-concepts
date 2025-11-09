# Defining a set

positions = {1 , 4 , 5 ,7 ,1 , 3 ,5 , 9, 7 , 4}

# printing the ype of positions

print(type(positions))

print(positions)

# To add elemnts in a set 

# we try adding the number 20 in the set

positions.add(20)
positions.add(30)
print(f"New set =  {positions}")


# we try deleting one of the added items using remove method

positions.remove(20)
print(f"New set after deleting =  {positions}")