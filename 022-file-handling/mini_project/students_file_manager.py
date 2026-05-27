# مشروع صغير إضافي - إدارة أسماء الطلاب داخل ملف
# الفكرة: حفظ أسماء الطلاب ثم قراءتها كسطور نظيفة.

STUDENTS_FILE = "data/mini_students.txt"

def save_student(name):
    with open(STUDENTS_FILE, "a", encoding="utf-8") as file:
        file.write(name + "\n")

def get_students():
    students = []

    with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            students.append(line.strip())

    return students

save_student("Ali")
save_student("Sara")
save_student("Omar")

students = get_students()

print("=" * 45)
print("Students File Manager")
print("=" * 45)

for student in students:
    print("-", student)

print("=" * 45)
