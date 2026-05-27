# حل تمرين 05

tasks = ["Study Python", "Practice files", "Review lesson"]

with open("data/my_tasks.txt", "w", encoding="utf-8") as file:
    for task in tasks:
        file.write(task + "\n")

print("Tasks saved")
