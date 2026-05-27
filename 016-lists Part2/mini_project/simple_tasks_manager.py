# مشروع صغير - مدير مهام بسيط باستخدام List
# الفكرة: تطبيق إنشاء قائمة، append، insert، remove، pop، len، for، slicing.

tasks = []

tasks.append("تعلم القوائم")
tasks.append("حل تمارين بايثون")
tasks.append("مراجعة الدرس")

print("=" * 45)
print("Tasks after append:")
for task in tasks:
    print("-", task)

tasks.insert(1, "مشاهدة مثال عملي")

print("\nTasks after insert:")
for task in tasks:
    print("-", task)

completed_task = tasks.pop()

print("\nCompleted task:", completed_task)
print("Remaining tasks count:", len(tasks))

task_to_remove = "حل تمارين بايثون"

if task_to_remove in tasks:
    tasks.remove(task_to_remove)

print("\nCurrent tasks:")
for task in tasks:
    print("-", task)

print("\nFirst two tasks:")
print(tasks[:2])

print("=" * 45)
