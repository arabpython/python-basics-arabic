# بايثون العرب - الدرس 22
# قراءة أسماء الطلاب مع تنظيف نهاية السطر

with open("data/students.txt", "r", encoding="utf-8") as file:
    for student in file:
        print(student.strip())
