#  In this utility function we define our 5 functions.

def add_tasks(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Added -> {task}")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("Your tasks are : \n")
        for i in range(len(tasks)):
            print(f"{i + 1} . {tasks[i]}")


def mark_tasks(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        print("You have empty tasks")
    else:
        num =int(input("Enter task number to mark as Done : "))
    if 1 <= num <= len(tasks):
        tasks[num - 1] += " -> COMPLETED"
        print(f"Task marked as Done")
    else:
        print("Invalid Task Number")
            


def delete_tasks(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        print("You have empty tasks")
    else:
        num =int(input("Enter task number to delete : "))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed}")
    else:
        print("Invalid Task Number")


def exit_application():
    pass
