# مشروع صغير ثالث - حفظ وقراءة المهام اليومية

TASKS_FILE = "data/mini_tasks.txt"

tasks = [
    "تعلم open",
    "تجربة read",
    "تجربة write",
    "مراجعة الفرق بين w و a"
]

with open(TASKS_FILE, "w", encoding="utf-8") as file:
    for task in tasks:
        file.write(task + "\n")

print("=" * 45)
print("Tasks File Project")
print("=" * 45)
print("المهام المحفوظة:")

with open(TASKS_FILE, "r", encoding="utf-8") as file:
    for task in file:
        print("-", task.strip())

print("=" * 45)
