# بايثون العرب - الدرس 22
# كتابة عناصر قائمة داخل ملف

tasks = ["Study Python", "Practice files", "Review lesson"]

with open("data/tasks_from_list.txt", "w", encoding="utf-8") as file:
    for task in tasks:
        file.write(task + "\n")

print("Tasks saved")
