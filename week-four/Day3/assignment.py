# Create a program that takes in a list of items with duplicates and returns
# 1. A tuple of the 1st 3 unique items
# 2. A set of all unique items

# A list of items of different datatypes
items = [1, "james", 1, "james", 2, 5, 7, "John", 2, 5, 8]

# Step 1: Remove duplicates while keeping order
unique_items = []
for i in items:
    if i not in unique_items:
        unique_items.append(i)

# Step 2: Create a tuple of the first 3 unique items
first_three_unique = tuple(unique_items[:3])

# Step 3: Create a set of all unique items
unique_set = set(unique_items)

# Step 4: Display results
print(f"Tuple of first 3 unique items: {first_three_unique}")
print(f"Set of all unique items: {unique_set}")
