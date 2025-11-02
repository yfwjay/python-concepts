# In this main python scripts we define the flow of our application

from menu import * 
from tasks import *


def main():
    tasks = []
    while True:
        menu_user()
        choice = get_user_input()

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_tasks(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            print("Goodbye you have exited the application")
            break
        else:
            print("Invalid Choice try again")


main()



