# We first generate a menu that will welcome the user to the CLI application
# The menu should also have choices that the user can select

def menu():
    print("\n WELCOME TO YOUR GROCERY LIST AND BUDGET TRACKER SYSTEM \n")
    print("1. Set a budget")
    print("2. Add Items to your List")
    print("3. View your Item List")
    print("4. Remove an Item from the List")
    print("5. Show Total Spent and Budget Left")
    print("6. Exit the Application")


def user_choice():
    return input("\nChoose an option (1-6) = ")


