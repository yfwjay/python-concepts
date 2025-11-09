# Inside here we define the functions for each option\

grocery_items = []

grocery_set = set()
budget = 0
def set_budget():
    global budget
    budget = int(input("Enter Your Groccery List Shopping budget = "))
    print(f"Your Budget is = {budget}")

def add_items():
    # We define a dictionary to be able to store our item , quantity and price
    name = input("Enter an Grocery Item: = ").strip().title()
    groc_quantity = int(input(f"Enter the Quantity of {name} = "))
    groc_price = int(input(f"Enter the price of one {name} = "))
    grocery_dict = {
        "Grocery_name" : name , 
        "Quantity" : groc_quantity , 
        "Price" : groc_price * groc_quantity
    }
    # Print statement to display to the user that it was a successful addition.
    print(f"Added {groc_quantity} {name} of price {groc_price} to your Grocery List.")
    # We append each grocery item to our dictionary
    grocery_items.append(grocery_dict)
    # We should also try and remove duplicates by having a set 
    grocery_set.add(name)

def view_items():
    # Now we want to display the grocery items.
    if len(grocery_items) == 0:
        print("You have no Groceries in your List")
        return
    print("-----YOUR GROCERIES INCLUDE------- \n")

    # We have to loop through our list
    for indx , grocery_dict in enumerate(grocery_items , start = 1):
        print(f"{indx}.{grocery_dict['Grocery_name']} ({grocery_dict['Quantity']}) = {grocery_dict['Price']} ")


def remove_item():
    if len(grocery_items) == 0:
        print("You have no items to remove.")
        return

    # Show current items
    view_items()

    user_choice = input("Select the number of the item to remove: ")

    # Check if the user typed a number
    if user_choice.isdigit():  # Only proceed if the input is all digits
        user_choice = int(user_choice)

        # Check if the number is within the valid range
        if user_choice >= 1 and user_choice <= len(grocery_items):
            removed_item = grocery_items.pop(user_choice - 1)
            grocery_set.remove(removed_item["Grocery_name"])
            print(f"Removed {removed_item['Grocery_name']} from your list.")
        else:
            print("Invalid number — no item with that number.")
    else:
        print("Please enter a valid number (e.g., 1, 2, 3...).")


def total_budget():
    total_spent = sum(item["Price"] for item in grocery_items)
    remaining = budget - total_spent
    print(f"Total spent: {total_spent}")
    print(f"Budget left: {remaining}")

def exit_application():
    print("You have successfully exited the application!!")