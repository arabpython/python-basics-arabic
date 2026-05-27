# بايثون العرب - الدرس 22
# تمرين الدرس: حفظ ثلاث مهام داخل ملف

tasks = ["تعلم فتح الملفات", "قراءة ملف نصي", "كتابة ملف جديد"]

with open("data/tasks.txt", "w", encoding="utf-8") as file:
    for task in tasks:
        file.write(task + "\n")

with open("data/tasks.txt", "r", encoding="utf-8") as file:
    print("المهام المحفوظة:")
    print(file.read())
