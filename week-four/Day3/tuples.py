# A tuple defination

positions = (1 , 5 , 8 , 7 , 6)

print(type(positions))  # to check if what we have defines is a tuple.


# Accessing elements in a tuple

for i in positions:
    # print(f"{[i + 1]} -> {i}")
    print(i)

# Another way of accessinf=g the elements by specifying the index
print(positions[1])

# Slicing a tuple
print(positions[2:])

# Unpacking a tuple

a , b , c, d , e = positions

print(positions)

