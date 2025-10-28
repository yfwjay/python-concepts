# Demonstration of 'continue' statement in a loop 

cost = [20 , 30 , 'sixty' , 10]
Total_cost = 0

for item in cost:
    if type(item) != int:
        continue
    Total_cost += item
    print(f"Added {item}, total is now {Total_cost}")
