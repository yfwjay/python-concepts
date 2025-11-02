tasks = []

while True:
    if len(tasks) <= 2:
        task = input("Enter a task : ")
        tasks.append(task)

        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    else:
        break

