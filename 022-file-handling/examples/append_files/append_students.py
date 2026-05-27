# بايثون العرب - الدرس 22
# إضافة أسماء طلاب إلى نهاية ملف

student_name = "Mona"

with open("data/students.txt", "a", encoding="utf-8") as file:
    file.write(student_name + "\n")

print("Student saved successfully")
