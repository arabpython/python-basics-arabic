# حل تمرين 08

tasks = ["Task 1", "Task 2", "Task 3"]

with open("data/tasks_practice.txt", "w", encoding="utf-8") as file:
    for task in tasks:
        file.write(task + "\n")

with open("data/tasks_practice.txt", "r", encoding="utf-8") as file:
    print("Saved tasks:")
    print(file.read())
