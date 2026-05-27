# بايثون العرب - الدرس 22
# تحويل أسطر الملف إلى قائمة نظيفة بدون \n

with open("data/students.txt", "r", encoding="utf-8") as file:
    students = file.readlines()

clean_students = []

for student in students:
    clean_students.append(student.strip())

print(clean_students)
