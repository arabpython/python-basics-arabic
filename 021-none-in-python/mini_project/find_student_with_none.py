# مشروع صغير - البحث عن طالب وإرجاع None عند عدم وجود نتيجة
# الفكرة: استخدام None للتعبير عن عدم وجود نتيجة واضحة.

def find_student(students, target_name):
    for student in students:
        if student["name"] == target_name:
            return student

    return None

students = [
    {"name": "Ali", "grade": 80},
    {"name": "Sara", "grade": 95},
    {"name": "Omar", "grade": 70},
]

target_name = "Mona"

result = find_student(students, target_name)

print("=" * 45)
print("Find Student With None")
print("=" * 45)

if result is None:
    print("الطالب غير موجود:", target_name)
else:
    print("تم العثور على الطالب")
    print("Name :", result["name"])
    print("Grade:", result["grade"])

print("=" * 45)
